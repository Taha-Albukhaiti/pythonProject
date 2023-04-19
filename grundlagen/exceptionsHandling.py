lists = [2, 3, "Hello", 0]


def rez(l, index):
    try:
        r = 1 / l[index]
    except IndexError:
        print("Falscher Index")
        r = None
    except (ZeroDivisionError, TypeError) as e:
        print(e)
        r = None
    except:
        print("Sonstige fehler!")
    else:
        return r
    finally:
        print(str(index),":  ",  str(r))

print(rez(lists, 0))
print(rez(lists, 3))
print(rez(lists, 2))
