# Fibonacci-Zahlen-Modul

def fib(n):    # schreibe Fibonacci-Folge bis n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # gib die Fibonacci-Folge zurück bis n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

