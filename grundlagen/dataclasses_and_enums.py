from dataclasses import dataclass


class Bogen:
    def __init__(self, name, preis, schaden):
        self.name = name
        self.preis = preis
        self.schaden = schaden

    def __str__(self):
        return f"Ich bin {self.name} und mein Preis ist {self.preis} und Schaden {self.schaden}"


bogen_a = Bogen("Guter Bogen", 500, 90)


@dataclass
class Bogen1:
    name: str
    preis: float
    schaden: int = 100


@dataclass
class MagicBogen(Bogen1):
    mag_dmg: int = 300


bogen_1 = Bogen1("Standard Bogen", 200, 90)
bogen_2 = MagicBogen("Standard Bogen", 200, 121)
print(bogen_1)
print(bogen_2)

from enum import Enum

class Waffen(Enum):
    S = "Schwert"
    B = "Bogen"
    A = "Axt"

print(repr(Waffen.S))