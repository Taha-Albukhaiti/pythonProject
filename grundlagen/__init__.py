# -------- Üben --------
import math
from math import pi
from collections import deque

knights = {'Gallahad': 'der Reine', 'Robin': 'der Mutige'}
for k, v in knights.items():
    print(k, v)
print()

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print()

a = ['spam', 'eggs', 100, 1234]
a[2] = a[2] + 23

a, b = 0, 1
while b < 10:
    print(b, end=' ')
    a, b = b, a + b
    # a = 1 und b = 1
    # a = 1 und b = 2
    # a = 2 und b = 3
    # a = 3 und b = 5
    # a = 5 und b = 8
    # a = 8 und b = 13
print()

# Die Längen einiger Zeichenketten ermitteln:
b = ['Katze', 'Fenster', 'rauswerfen']
for x in b:
    print(x, len(x))

for x in b[:]:
    if len(x) > 7: b.insert(0, x)
print(b)

# range(beginn, ende, Schrittweite)
for i in range(3, 10, 3):
    print(i, end=" ")
print()
print()

for i in range(len(b)):
    print(i, b[i])

# umgekehrt ausgeben
for i in reversed(range(1, 10, 2)):
    print(i)

# Um über mehrere Sequenzen gleichzeitig zu iterieren
questions = ['Name', 'Auftrag']
answers = ['Lancelot', 'die Suche nach dem Heiligen Gral']
for q, a in zip(questions, answers):
    print('Was ist dein {0}?  Er ist {1}.'.format(q, a))
print()

# Iterieren in sortierter Reihenfolge
basket = ['Apfel', 'Orange', 'Apfel', 'Birne', 'Orange', 'Banane']
for f in sorted(set(basket)):
    print(f)
print()

string1, string2, string3 = '', 'Trondheim', 'Hammer Tanz'
non_null = string1 or string2 or string3
print(non_null)


# Funktion Fibonacci-Folge
def fib(n):  # die Fibonacci-Folge bis n ausgeben
    """Print the Fibonacci series up to n."""
    resu = list()
    m, y = 0, 1
    while m < n:
        resu.append(m)
        m, y = y, m + y
    return resu


# Jetzt rufen wir die Funktion auf, die wir gerade definiert haben:
fib(2000)
print()
print()


def ask_ok(prompt, retries=4, complaint='Bitte Ja oder Nein!'):
    while True:
        ok = input(prompt)
        if ok in ('j', 'J', 'ja', 'Ja'): return True
        if ok in ('n', 'N', 'ne', 'Ne', 'Nein'): return False
        retries = retries - 1
        if retries < 0:
            raise IOError('Benutzer abgelehnt!')
        print(complaint)


# ask_ok("Willst du wirklich aufhören?")
# 360°/(2π)

def bogen_Mass():
    rad = float(input("Winkel in Bogenmass eingeben: "))
    deg = rad * 180.0 / pi
    grad = int(deg)
    bogenmin = int((deg - grad) * 60)
    bogenmin = ((deg - grad) * 60 - bogenmin) * 60
    print(rad, " rad = ", grad, "°", bogenmin, "'", bogenmin, "\"", sep="")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Haben sie", kind, "?")
    print("-- Tut mir leid,", kind, "ist leider gerade aus.")
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "Der ist sehr flüssig, mein Herr.",
           "Der ist wirklich sehr, SEHR flüssig, mein Herr.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -------------- Listen ---------------
print()
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(-1))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

# ------------ Listen können als Stack verwendet werden also (Last in, First out) -------------
stack = [2, 3, 8]
stack.append(9)
stack.append(10)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# ------------ Listen können als Queue verwendet werden also (First in, first out) -------------
# Allerdings sind Listen nicht effizient für diesen Zweck. Während append() und pop() am Ende der Liste schnell sind,
# sind insert() und pop() am Anfang der Liste langsam (da alle anderen Elemente um eine Stelle verschoben werden müssen).
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry kommt an
queue.append("Graham")  # Graham kommt an
queue.popleft()
print(queue)

# ------------ List Comprehensions -------------
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
squares1 = [x ** 2 for x in range(10)]
squares2 = list(map(lambda y: y ** 2, range(10)))
print(squares1)
print(squares2)

# ---- das und die for Schleife machen dasselbe ---
squares3 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares3)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

vec = [-4, -2, 0, 2, 4]
# erzeuge eine neue Liste mit den verdoppelten Werten
test = [x * 2 for x in vec]
print(test)
# filtere die negativen Zahlen heraus
test = [x for x in vec if x >= 0]
print(test)
# wende eine Funktion auf alle Elemente an
test = [abs(x) for x in vec]
print(test)
# rufe eine Methode auf allen Elementen auf
freshFruit = ['  banana', '  loganberry ', 'passion fruit      ']
freshFruit1 = [weapon.strip() for weapon in freshFruit]
print(freshFruit1)
# erstelle eine Liste von 2-Tupeln der Form (zahl, quadrat)
quadrat = [(x, x ** 2) for x in range(10)]
print(quadrat)
# das Tupel muss geklammert werden, sonst wird ein Fehler erzeugt
# verflache eine Liste durch eine LC mit zwei 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test1 = [num for elem in vec for num in elem]
print(test1)
combs1 = []
for elem in vec:
    for num in elem:
        combs1.append(num)
print(combs1)

# komplexer
test2 = [str(round(pi, i)) for i in range(1, 6)]
print(test2)
print()
# eine 3x4 Matrix mit drei Listen der Länge vier
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matr = [[row[i] for row in matrix] for i in range(4)]
print(matr)

matr1 = []
for i in range(len(matrix[0])):  # 4
    row = []
    for j in range(len(matrix)):  # 3
        row.append(matrix[j][i])
    matr1.append(row)

print(matr1)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

li = list(zip(*matrix))
print(li)
list(range(3, 6))  # normaler Aufruf mit getrennten Argumenten
args = [3, 6]
list(range(*args))  # Aufruf mit Argumenten, die aus einer Liste ausgepackt werden


def parrot(voltage, state=' völlig steif',
           action='fliegen', type='norwegische Blauling'):
    print("-- Der Vogel würde selbst dann nicht", action, end=' ')
    print("selbst wenn Sie ihm ", voltage, "Volt durch den Schnabel jagen täten.")
    print("-- Er is", state, "!")
    print("-- Er is", type, "!")


d = {"voltage": "vier Millionen", "state": "verdammt nochmal tot!", "action": "FLIEGEN"}
print(parrot(**d))
print()

# Listenelement durch seinen Index, statt durch seinen Wert zu löschen
# del-Anweisung. Sie unterscheidet sich von der pop()-Methode, da sie keinen Wert zurückgibt.
# del kann auch dazu benutzt werden, ganze Variablen zu löschen
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a

# Tupel
t = 12345, 54321, 'Hallo!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
# Tupel sind unveränderlich:
# aber sie können veränderliche Objekte enthalten:
v = ([1, 2, 3], [3, 2, 1])
print(v)
# was passiert mit einem leeren Tupel und oder einen mit nur einem Wert
empty = ()
singleton = 'Hallo',  # <-- das angehängte Komma nicht vergessen
print(len(empty))
print(len(singleton))
print(singleton)
x, y, z = t
print(y)

# --------------------- Mengen(sets) ---------------------
print()
basket = {'Apfel', 'Orange', 'Apfel', 'Birne', 'Orange', 'Banane'}
print(basket)
print('Orange' in basket)  # schnelles Testen auf Mitgliedschaft
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # in a aber nicht in b
print(a | b)  # in a oder b, Vereinigung
print(a & b)  # sowohl in a, als auch in b Schnittmenge
print(a ^ b)  # entweder in a oder b

# --------------------- Dictionaries ---------------------
# Anders als Sequenzen, die über Zahlen indizierbar sind, sind Dictionaries durch Schlüssel (keys)
print()
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x ** 2 for x in (2, 4, 6)})
# Einfacher
print(dict(sape=4139, guido=4127, jack=4098))

# Wenn man über Dictionaries iteriert,
# lassen sich der Schlüssel und der entsprechende Wert gleichzeitig durch die Methode items() abrufen.

knights = {'Gallahad': 'der Reine', 'Robin': 'der Mutige'}
for k, v in knights.items():
    print(k, v)

# Iteriert man über eine Sequenz,
# lassen sich der Index und das entsprechende Objekt gleichzeitig über die Funktion enumerate() abrufen.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Um über mehrere Sequenzen gleichzeitig zu iterieren,
# können die Einträge mithilfe der zip()-Funktion gruppiert werden.

questions = ['Name', 'Auftrag']
answers = ['Lancelot', 'die Suche nach dem Heiligen Gral']
for q, b in zip(questions, answers):
    print('Was ist dein {0}?  Er ist {1}.'.format(q, b))
# Über eine Sequenz in der umgekehrten Reihenfolge
for i in reversed(range(1, 10, 2)):
    print(i)

# Eine Sequenz in einer sortieren Reihenfolge, ohne die ursprüngliche Sequenz anzurühren mit der Methode sorted()
basket = ['Apfel', 'Orange', 'Apfel', 'Birne', 'Orange', 'Banane']
for f in sorted(set(basket)):
    print(f)


# ------------- Aufgaben ------------
def median(a, b, c):
    if b < a <= c or b > a >= c:
        return a
    elif a < b <= c or a > b >= c:
        return b
    else:
        return c


print(median(11, 11, 21))
print(median(3, 2, 1))
print(median(1, 3, 9))
print(median(1, 3, 3))

s = "String"
print(s.replace(s, "Hallo"))
print(s * 2)
ss = {'jack': 4098, 'sape': 4139}
print(ss)
x = 10 * 3.25
y = 200 * 200
s = 'Der Wert von x ist ' + repr(x) + ', und y ist ' + repr(y) + '...'
print(s)
hello = 'Hallo Welt\n'
hellos = repr(hello)
print(hellos)
print(str(hellos))
print(repr((x, y, ('spam', 'eggs'))))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4), end=' ')
    # Achte auf die Benutzung von 'end' in der vorherigen Zeile
    print(repr(x * x * x * x).rjust(5))
print()
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('Der Wert von Pi ist ungefähr {0:.3f}.'.format(math.pi))
print('Der Wert von Pi ist ungefähr', math.pi)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
print()


# Beispiel zu Gültigkeitsbereichen und Namensräumen
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("Nach der lokalen Zuweisung:", spam)
    do_nonlocal()
    print("Nach der nonlocal Zuweisung:", spam)
    do_global()
    print("Nach der global Zuweisung:", spam)


scope_test()
print("Im globalen Gültigkeitsbereich:", spam)
Faker.seed(0)
for _ in range(5):
    fake.pybool()
