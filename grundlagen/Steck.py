from typing import List, Any


class Steck:
    """
    Doc
    """
    items: list[Any]

    def __init__(self):
        self.items = []

    def push(self, arg):
        self.items.append(arg)

    def pop(self):
        rem = self.items[-1]
        del self.items[-1]
        return rem

    def empty(self):
        return len(self.items) == 0



class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hallo Welt'


s = MyClass()
s.f()
print(MyClass.f(s))

print(s.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
