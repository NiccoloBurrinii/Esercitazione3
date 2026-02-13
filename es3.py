import math

class Forma():
    def perimetro(self):
        pass

    def info(self):
        pass

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def perimetro(self):
        return 2 * 3.14 * self.raggio

    def area(self):
        return 3.14 * self.raggio ** 2
    
    def info(self):
        print(f"Forma: Cerchio, Raggio: {self.raggio}, Perimetro: {self.perimetro()}, Area: {self.area()}")

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

    def area(self):
        return self.base * self.altezza
    
    def info(self):
        print(f"Forma: Rettangolo, Base: {self.base}, Altezza: {self.altezza}, Perimetro: {self.perimetro()}, Area: {self.area()}")


class Triangolo(Forma):
    def __init__(self, lato1, lato2, lato3):
        self.lato1 = float(lato1)
        self.lato2 = float(lato2)
        self.lato3 = float(lato3)
        if any(l <= 0 for l in (self.lato1, self.lato2, self.lato3)):
            raise ValueError("I lati devono essere maggiori di zero")
        if not (self.lato1 + self.lato2 > self.lato3 and
                self.lato1 + self.lato3 > self.lato2 and
                self.lato2 + self.lato3 > self.lato1):
            raise ValueError("I lati non formano un triangolo valido")

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lato1) * (s - self.lato2) * (s - self.lato3))

    def info(self):
        print(f"Forma: Triangolo, Lati: {self.lato1}, {self.lato2}, {self.lato3}, Perimetro: {self.perimetro()}, Area: {self.area()}")

def calcola_area_totale(forme):
    """Calcola somma aree di lista forme (polimorfismo)"""
    return sum(f.area() for f in forme)

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