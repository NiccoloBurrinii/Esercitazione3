# LEZIONE 29 - ESERCITAZIONI
## Ereditarietà e Polimorfismo

**Modalità:** Individuale | **Durata:** 2 ore (60 min guidate + 60 min autonome)

---

## 📋 ESERCITAZIONI GUIDATE (60 minuti)

### Esercizio 1 - Gerarchia Veicoli (20 minuti)

#### Descrizione
Creare una gerarchia di classi per modellare diversi tipi di veicoli usando ereditarietà.

#### Requisiti

**Classe Veicolo (base):**
- `__init__(self, marca, modello, anno)`
  - Inizializza attributi comuni
  - `km = 0` inizialmente

- `info(self)`
  - Restituisce stringa con informazioni base

- `guida(self, km)`
  - Aggiunge km al totale

**Classe Auto(Veicolo):**
- `__init__(self, marca, modello, anno, num_porte)`
  - Chiama super().__init__()
  - Aggiunge num_porte

- `info(self)` (override parziale)
  - Usa super().info() e aggiunge num_porte

**Classe Moto(Veicolo):**
- `__init__(self, marca, modello, anno, tipo)`
  - tipo: "sportiva", "cruiser", "touring"
  - Chiama super().__init__()

- `impennata(self)`
  - Stampa messaggio

**Classe Camion(Veicolo):**
- `__init__(self, marca, modello, anno, capacita_carico)`
  - capacita_carico in tonnellate
  - Chiama super().__init__()

- `carica(self, peso)`
  - Verifica capacità e carica

#### Esempio di Utilizzo
```python
auto = Auto("Fiat", "500", 2020, 3)
moto = Moto("Ducati", "Monster", 2021, "sportiva")
camion = Camion("Iveco", "Daily", 2019, 3.5)

veicoli = [auto, moto, camion]

# Polimorfismo: tutti hanno metodo info()
for v in veicoli:
    print(v.info())
    
auto.guida(100)
moto.impennata()
camion.carica(2.5)
```

#### Output Atteso
```
Fiat 500 (2020) - 0 km - 3 porte
Ducati Monster (2021) - 0 km - Tipo: sportiva
Iveco Daily (2019) - 0 km - Capacità: 3.5 t

Auto guidata per 100 km. Totale: 100 km
La moto fa un'impennata!
Caricati 2.5 t sul camion
```

#### Hint
- Usa `super().__init__(marca, modello, anno)` nelle classi derivate
- Override parziale: `base_info = super().info()`
- Ogni classe può avere metodi propri specializzati

---

### Esercizio 2 - Sistema Pagamenti (20 minuti)

#### Descrizione
Creare sistema di pagamento polimorfo con diversi metodi.

#### Requisiti

**Classe Pagamento (base astratta):**
- `__init__(self, importo)`
  - Inizializza importo
  - `completato = False`

- `processa(self)` (metodo da sovrascrivere)
  - Raise NotImplementedError
  - Sottoclassi devono implementarlo

- `is_completato(self)`
  - Restituisce stato completamento

**Classe CartaDiCredito(Pagamento):**
- `__init__(self, importo, numero_carta, cvv)`
  - Chiama super().__init__()
  - Salva numero_carta e cvv

- `processa(self)` (override)
  - Valida carta (lunghezza 16, CVV 3 cifre)
  - Simula pagamento
  - Imposta completato = True

**Classe PayPal(Pagamento):**
- `__init__(self, importo, email)`
  - Chiama super().__init__()
  - Salva email

- `processa(self)` (override)
  - Valida email (contiene '@')
  - Simula pagamento
  - Imposta completato = True

**Classe Bitcoin(Pagamento):**
- `__init__(self, importo, wallet_address)`
  - Chiama super().__init__()
  - Salva wallet_address

- `processa(self)` (override)
  - Valida wallet (lunghezza >= 26)
  - Simula pagamento
  - Imposta completato = True

#### Esempio di Utilizzo
```python
pagamenti = [
    CartaDiCredito(100, "1234567890123456", "123"),
    PayPal(50, "user@email.com"),
    Bitcoin(200, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
]

# Polimorfismo: tutti hanno processa()
for pag in pagamenti:
    print(f"Processando pagamento di €{pag.importo}...")
    pag.processa()
    print(f"Completato: {pag.is_completato()}\n")
```

#### Output Atteso
```
Processando pagamento di €100...
Pagamento con carta *3456 approvato
Completato: True

Processando pagamento di €50...
Pagamento PayPal a user@email.com approvato
Completato: True

Processando pagamento di €200...
Pagamento Bitcoin a wallet 1A1z...fNa approvato
Completato: True
```

#### Hint
- Metodo base `processa()`: `raise NotImplementedError("Metodo da implementare")`
- Validazione semplice: `len(numero_carta) == 16`
- Mascheramento carta: mostra solo ultime 4 cifre
- isinstance() utile per identificare tipo pagamento

---

### Esercizio 3 - Forme Geometriche (20 minuti)

#### Descrizione
Creare gerarchia di forme geometriche con calcolo area e perimetro polimorfo.

#### Requisiti

**Classe Forma (base):**
- `area(self)` 
  - Raise NotImplementedError

- `perimetro(self)`
  - Raise NotImplementedError

- `info(self)`
  - Stampa tipo forma, area e perimetro

**Classe Cerchio(Forma):**
- `__init__(self, raggio)`
  - Salva raggio

- `area(self)` (override)
  - π × raggio²

- `perimetro(self)` (override)
  - 2 × π × raggio

**Classe Rettangolo(Forma):**
- `__init__(self, base, altezza)`
  - Salva dimensioni

- `area(self)` (override)
  - base × altezza

- `perimetro(self)` (override)
  - 2 × (base + altezza)

**Classe Triangolo(Forma):**
- `__init__(self, lato1, lato2, lato3)`
  - Salva tre lati
  - Valida che formino triangolo

- `area(self)` (override)
  - Formula di Erone: √[s(s-a)(s-b)(s-c)]
  - s = (a+b+c)/2

- `perimetro(self)` (override)
  - lato1 + lato2 + lato3

#### Funzione Helper
```python
def calcola_area_totale(forme):
    """Calcola somma aree di lista forme (polimorfismo)"""
    return sum(f.area() for f in forme)
```

#### Esempio di Utilizzo
```python
import math

forme = [
    Cerchio(5),
    Rettangolo(4, 6),
    Triangolo(3, 4, 5)
]

# Polimorfismo
for forma in forme:
    forma.info()

print(f"\nArea totale: {calcola_area_totale(forme):.2f}")
```

#### Output Atteso
```
Cerchio: Area = 78.54, Perimetro = 31.42
Rettangolo: Area = 24.00, Perimetro = 20.00
Triangolo: Area = 6.00, Perimetro = 12.00

Area totale: 108.54
```

#### Hint Formula Erone
```python
s = (lato1 + lato2 + lato3) / 2
area = math.sqrt(s * (s - lato1) * (s - lato2) * (s - lato3))
```

#### Hint Validazione Triangolo
```python
# Disuguaglianza triangolare
return (lato1 + lato2 > lato3 and 
        lato1 + lato3 > lato2 and 
        lato2 + lato3 > lato1)
```

---

## 🎯 ESERCITAZIONI AUTONOME (60 minuti)

### Esercizio 4 - Gerarchia Dipendenti (20 minuti)

#### Descrizione
Creare sistema gerarchico dipendenti con calcolo stipendio polimorfo.

#### Requisiti

**Classe Dipendente (base):**
- `__init__(self, nome, codice, stipendio_base)`
- `calcola_stipendio(self)` → restituisce stipendio_base
- `info(self)` → informazioni dipendente

**Classe Manager(Dipendente):**
- `__init__(self, nome, codice, stipendio_base, bonus)`
- `calcola_stipendio(self)` (override)
  - stipendio_base + bonus

**Classe Sviluppatore(Dipendente):**
- `__init__(self, nome, codice, stipendio_base, linguaggi)`
  - linguaggi: lista linguaggi conosciuti
- `aggiungi_linguaggio(self, linguaggio)`
- `calcola_stipendio(self)` (override)
  - stipendio_base + (100 × numero_linguaggi)

**Classe Stagista(Dipendente):**
- `__init__(self, nome, codice, ore_mensili, tariffa_oraria)`
- `calcola_stipendio(self)` (override)
  - ore_mensili × tariffa_oraria

#### Test
```python
dipendenti = [
    Manager("Alice", "M001", 3000, 500),
    Sviluppatore("Bob", "S001", 2500, ["Python", "Java"]),
    Stagista("Carlo", "ST001", 80, 15)
]

totale_stipendi = sum(d.calcola_stipendio() for d in dipendenti)

for d in dipendenti:
    print(f"{d.nome}: €{d.calcola_stipendio()}")

print(f"\nTotale stipendi: €{totale_stipendi}")
```

#### Output Atteso
```
Alice: €3500
Bob: €2700
Carlo: €1200

Totale stipendi: €7400
```

---

### Esercizio 5 - Account Bancari (20 minuti)

#### Descrizione
Creare diversi tipi di account bancari con logica interesse/commissioni specifica.

#### Requisiti

**Classe Account (base):**
- `__init__(self, titolare, saldo=0)`
- `deposita(self, importo)`
- `preleva(self, importo)`
- `applica_interessi_mensili(self)` → da sovrascrivere

**Classe ContoCorrente(Account):**
- `commissione_prelievo = 2` (euro per prelievo)
- `preleva(self, importo)` (override)
  - Sottrae importo + commissione
- `applica_interessi_mensili(self)` (override)
  - Nessun interesse (return 0)

**Classe ContoRisparmio(Account):**
- `__init__(self, titolare, saldo, tasso_interesse)`
  - tasso_interesse: es. 0.02 per 2% annuo
- `preleva(self, importo)` (override)
  - Max 3 prelievi al mese (traccia contatore)
  - Se supera: commissione extra €5
- `applica_interessi_mensili(self)` (override)
  - Aggiunge saldo × (tasso_interesse / 12)

**Classe ContoInvestimento(Account):**
- `__init__(self, titolare, saldo, rischio)`
  - rischio: "basso", "medio", "alto"
- `applica_interessi_mensili(self)` (override)
  - Rendimento casuale basato su rischio
  - Basso: 0-2%, Medio: -1-4%, Alto: -5-10%

#### Test
```python
conti = [
    ContoCorrente("Mario", 1000),
    ContoRisparmio("Anna", 5000, 0.03),
    ContoInvestimento("Luigi", 10000, "medio")
]

# Simula mese
for conto in conti:
    conto.deposita(100)
    conto.preleva(50)
    interessi = conto.applica_interessi_mensili()
    print(f"{conto.titolare}: Saldo €{conto.saldo:.2f}, Interessi €{interessi:.2f}")
```

---

### Esercizio 6 - Challenge: E-commerce con Spedizioni (20 minuti)

#### Descrizione
Sistema e-commerce con calcolo spedizione polimorfo basato su tipo ordine.

#### Requisiti

**Classe Ordine (base):**
- `__init__(self, id_ordine, prodotti, indirizzo)`
  - prodotti: lista dizionari {"nome": ..., "prezzo": ..., "peso": ...}
- `totale_prodotti(self)` → somma prezzi
- `peso_totale(self)` → somma pesi
- `costo_spedizione(self)` → da sovrascrivere
- `totale_ordine(self)` → totale_prodotti + costo_spedizione

**Classe OrdineStandard(Ordine):**
- `costo_spedizione(self)` (override)
  - €5 fisso se totale < €50
  - Gratis se totale >= €50

**Classe OrdineExpress(Ordine):**
- `__init__(self, ..., giorni_consegna)`
  - giorni_consegna: 1-3
- `costo_spedizione(self)` (override)
  - 1 giorno: €15
  - 2 giorni: €10
  - 3 giorni: €7

**Classe OrdineInternazionale(Ordine):**
- `__init__(self, ..., paese)`
- `costo_spedizione(self)` (override)
  - Europa: €20 + €2/kg
  - Extra-EU: €35 + €5/kg

#### Test
```python
prodotti = [
    {"nome": "Libro", "prezzo": 15, "peso": 0.5},
    {"nome": "Cuffie", "prezzo": 30, "peso": 0.3}
]

ordini = [
    OrdineStandard("ORD001", prodotti, "Via Roma 1"),
    OrdineExpress("ORD002", prodotti, "Via Milano 2", giorni_consegna=1),
    OrdineInternazionale("ORD003", prodotti, "Via Parigi 3", paese="Francia")
]

for ordine in ordini:
    print(f"{ordine.id_ordine}:")
    print(f"  Prodotti: €{ordine.totale_prodotti()}")
    print(f"  Spedizione: €{ordine.costo_spedizione()}")
    print(f"  TOTALE: €{ordine.totale_ordine()}\n")
```

#### Output Atteso
```
ORD001:
  Prodotti: €45
  Spedizione: €5
  TOTALE: €50

ORD002:
  Prodotti: €45
  Spedizione: €15
  TOTALE: €60

ORD003:
  Prodotti: €45
  Spedizione: €21.6
  TOTALE: €66.6
```

---

## 📝 NOTE PER LO STUDENTE

### Concetti Chiave

1. **Ereditarietà**
   - `class Derivata(Base):`
   - Relazione "è un"
   - Riuso codice base

2. **super()**
   - Chiama metodi classe base
   - SEMPRE in `__init__` di derivata
   - `super().__init__(...)`

3. **Override**
   - Totale: ridefinisci completamente
   - Parziale: usa `super().metodo()` + aggiunte

4. **Polimorfismo**
   - Stesso metodo, comportamenti diversi
   - Liste di oggetti diversi con interfaccia comune

### Pattern Comune Ereditarietà

```python
class Base:
    def __init__(self, param_base):
        self.param_base = param_base
    
    def metodo_comune(self):
        # Implementazione base
        pass

class Derivata(Base):
    def __init__(self, param_base, param_derivata):
        super().__init__(param_base)  # Chiama base
        self.param_derivata = param_derivata
    
    def metodo_comune(self):  # Override parziale
        super().metodo_comune()  # Riusa base
        # Aggiunge logica propria
    
    def metodo_proprio(self):
        # Solo in Derivata
        pass
```

### Errori da Evitare

1. **Dimenticare super().__init__()**
   ```python
   # SBAGLIATO
   class Derivata(Base):
       def __init__(self, x, y):
           self.y = y  # Attributi base non inizializzati!
   
   # CORRETTO
   class Derivata(Base):
       def __init__(self, x, y):
           super().__init__(x)
           self.y = y
   ```

2. **Override che rompe contratto**
   ```python
   # Base restituisce int
   def metodo(self):
       return 42
   
   # Derivata non deve restituire tipo diverso
   def metodo(self):
       return "stringa"  # PROBLEMATICO
   ```

3. **Ereditare solo per riuso**
   - Deve esserci vera relazione "è un"
   - Altrimenti usa composizione

### Comandi Utili

```python
# Type checking
isinstance(obj, Classe)
issubclass(Derivata, Base)

# Visualizzare MRO
Classe.__mro__
Classe.mro()

# Verificare attributi
hasattr(obj, 'attributo')
```

---

## ✅ CHECKLIST COMPLETAMENTO

- [ ] Classe base definita correttamente
- [ ] Classi derivate usano super().__init__()
- [ ] Override fatto dove necessario
- [ ] Polimorfismo testato con lista oggetti diversi
- [ ] isinstance/issubclass usati dove appropriato
- [ ] Nomi metodi consistenti per polimorfismo
- [ ] Documentazione (docstring) presente

---

**Buon lavoro con l'ereditarietà! 🧬**
