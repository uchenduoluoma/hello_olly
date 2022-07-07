'''function syntax --> def name():
'''


def n_point2Binary(x, base):
    decPlace = len(str(x)) - 2
    b = ["."]
    while decPlace > 0:
        x = x * base
        b.append(int(x))
        x = x - int(x)
        decPlace -= 1
    return b


def decimalint_to_binary(x, base):
    b = []
    while x != 0:
        b.insert(0, x % base)
        x = x // base
    return (b)


def is_contained(source, term="."):
    return term in source


def point_split(x):
    L = x.split(".")
    return (L[0]), ("0." + L[1])


def InverseBaseFormatter(x):
    dict = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35
    }
    L = []
    for i in x:
        if i.isalpha():
            i = dict[i]
        L.append(int(i))
    return L


def decimal_to_base(x, base=2):
    x = str(x)
    if is_contained(x):
        intPart, decPart = point_split(x)
        a = decimalint_to_binary(intPart, base) + n_point2Binary(decPart, base)
        a = InverseBaseFormatter(a)
        return (a)
    else:
        a = decimalint_to_binary(int(x), base)
        a = InverseBaseFormatter(a)
        return (a)

InverseBaseFormatter()




""" for i in decimal_to_base(2589644346.8989754325,36):
    print(i, end="") """


