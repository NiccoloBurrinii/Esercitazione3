class Veicolo():
    def __init__ (self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.km = 0

    def info(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Km: {self.km}")

    def guida(self, km):
        if km > 0:
            self.km += km
            print(f"Hai guidato per {km} km. Totale km: {self.km}")
        else:
            print("I chilometri percorsi devono essere un numero positivo.")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, num_porte):
        super().__init__(marca, modello, anno)
        self.num_porte = num_porte

    def info(self):
        super().info()
        print(f"Numero di porte: {self.num_porte}")

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        if tipo in ["sportiva", "cruiser", "touring"]:
            self.tipo = tipo
        else:
            raise ValueError("Tipo di moto non valido.")

    def impennata(self):
        print(f"{self.marca} {self.modello} sta facendo un'impennata!")

class Camion(Veicolo):
    def __init__(self, marca, modello, anno, capacità):
        super().__init__(marca, modello, anno)
        self.capacità = capacità

    def carica(self, peso):
        if peso <= self.capacità:
            print(f"Caricando {peso} kg nel camion.")
        else:
            print("Peso eccessivo! Non è possibile caricare.")

auto = Auto("Fiat", "500", 2020, 3)
moto = Moto("Ducati", "Monster", 2021, "sportiva")
camion = Camion("Iveco", "Daily", 2019, 3.5)

veicoli = [auto, moto, camion]

# Polimorfismo: tutti hanno metodo info()
for v in veicoli:
    v.info()
    
auto.guida(100)
moto.impennata()
camion.carica(2.5)