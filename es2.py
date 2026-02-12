from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, importo):
        self.importo = importo
        self.completato = False

    @abstractmethod
    def processa(self):
        pass

    def is_completato(self):
        return self.completato
    
class CartaDiCredito(Pagamento):
    def __init__(self, importo, numero_carta, ccv):
        super().__init__(importo)
        self.numero_carta = numero_carta
        self.ccv = ccv
    
    def processa(self):
        if len(self.numero_carta) == 16 and len(self.ccv) == 3:
            if (self.numero_carta.isdigit() and self.ccv.isdigit()):
                self.completato = True
                num_cartaFinale = self.numero_carta[-4:]
                print(f"Pagamento di {self.importo}€ con carta *{num_cartaFinale} completato.")
            else:
                print("Numero carta e CCV devono essere numerici.")
        else:
            print("Numero carta o CCV non validi.")

class PayPal(Pagamento):
    def __init__(self, importo, email):
        super().__init__(importo)
        self.email = email
    
    def processa(self):
        if "@" in self.email and "." in self.email:
            self.completato = True
            print(f"Pagamento di {self.importo}€ con PayPal a {self.email}.")
        else:
            print("Email non valida.")

class Bitcoin(Pagamento):
    def __init__(self, importo, wallet_address):
        super().__init__(importo)
        self.wallet_address = wallet_address
    
    def processa(self):
        if len(self.wallet_address) >= 26 and len(self.wallet_address) <= 35:
            self.completato = True
            wallet_finale = self.wallet_address[4:-4] #fixare
            print(f"Pagamento di {self.importo}€ con Bitcoin a {wallet_finale}.")
        else:
            print("Indirizzo wallet non valido.")

# Esempio di utilizzo

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