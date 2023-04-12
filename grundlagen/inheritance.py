class BasePlyer:

    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        print(f"Ich bin  und laufe ....")


class Archer(BasePlyer):

    def __init__(self, hp, arrows):
        super().__init__(hp=hp)
        self.arrows = arrows

class Wizard(BasePlyer):
    pass

class NoUpdateDictionary(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Key existiert schon!")
        super().__setitem__(key, value)

n = NoUpdateDictionary();
n["Klar"] = 123
print(n)
n["Klar"] = 2331

archer = Archer(100, 11)
wizard = Wizard(33)
wizard.walk()
print(archer.hp)

x = {"bla": 123}
x["bla"] = 222
print(x)