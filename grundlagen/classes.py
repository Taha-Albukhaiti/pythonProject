class Archer:

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self._arrows = arrows # Damit heißt es private Attribut wie in Java

    def wolk(self):
        print(f"Ich bin {self}!!")

    def shoot(self):
        if self._arrows > 0:
            self._arrows -= 1
            print(f"Bogenschütze hat geschossen, noch {self._arrows} Pfeile übrig")
        else:
            print(f"Der Bogenschütze hat kein Pfeile mehr!")

    @classmethod
    def sayHello(cls):
        print("Hello! Welcome")
        print("______________")
    @staticmethod
    def work():
        print("Have fun!")
        print("__________")

    @classmethod
    def from_data(cls, hp, mana, arrows):
        return cls(hp, mana, arrows) # Das Klassen Aufruf wie Archer

archer1 = Archer.from_data(100, 2, 4)
archer1.shoot()

Archer.sayHello()
Archer.work()
arch = Archer(100, 3, 5)
arch.shoot()


