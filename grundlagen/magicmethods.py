class Archer:

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    # toString Methode
    def __str__(self):
        return f"Archer mit {self.hp} HP und {self.mana} Mana mit {self.arrows} Pfeilen"

    # toString Methode, falls __str__ nicht da ist.
    def __repr__(self):
        return f"Archer({self.hp}, {self.mana}, {self.arrows})"

    # vergleicht, ob zwei Objekte gleich sind
    def __eq__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp == other.hp and self.mana == other.mana and self.arrows == other.arrows

    # prüfen ob self > other
    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp and self.mana > other.mana and self.arrows > other.arrows

    # prüfen ob self >= other
    def __ge__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp >= other.hp and self.mana >= other.mana and self.arrows >= other.arrows

    # erzeugt ein Hashwert
    def __hash__(self):
        return hash((self.hp, self.mana, self.arrows))


class Company:
    def __init__(self, size):
        self.archers = []
        self.size = size
        self.index = 0

    def addArcher(self, archer):
        if not isinstance(archer, Archer):
            raise ValueError("Nur Archer in Company erlaubt")
        if len(self.archers) >= self.size:
            raise ValueError("Company ist voll")
        self.archers.append(archer)

    # addiere ein Objekt zu den Objekten
    def __add__(self, other):
        if not isinstance(other, Archer):
            raise ValueError("Nur Archer in Company erlaubt")
        new_company = Company(self.size)
        for a in self.archers:
            new_company.addArcher(a)
        new_company.addArcher(other)
        return new_company

    # addiere ein Objekt zu den Objekten aber andere Reihenfolge
    def __radd__(self, other):
        return self + other

    # um die Company Liste zu iterieren. Die List wird zu einem Iterable
    def __iter__(self):
        return iter(self.archers)

    # das was aus __iter__ returned wird hier verwendet
    def __next__(self):
        if self.index > len(self.archers):
            raise StopIteration
        new_archers = next(self)# das kommt vo  __iter__
        self.index += 1
        return new_archers

archer = Archer(1000, 22, 300)
archer1 = Archer(100, 4, 3)
archer2 = Archer(300, 4, 22)
archer3 = Archer(300, 4, 22)
print(archer.__eq__(archer1))
print(archer.__eq__(22))
print(archer)
print(archer.__repr__())
print(archer > archer2)
print(archer <= archer2)
# Hashing
print(hash(archer))
archers = {archer: "Happy", archer1: "Depressed", archer2: "Angry"}

company = Company(3)

company.addArcher(archer1)
company.addArcher(archer2)

# new_company = company + archer
new_company = archer + company
print(company.archers)
print(new_company.archers)

for solider in new_company:
    print(solider)
