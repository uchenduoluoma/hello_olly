'''function syntax --> def name():
'''
import mpmath.libmp


def point2Binary(x,base):
    decPlace = len(str(x)) -2
    b=["."]
    while decPlace>0:
        x=x*base
        b.append(int(x))
        x = x - int(x)
        decPlace -=1
    return b


def decimalint_to_binary(x,base):
    b = []
    while x!=0:
        b.insert(0,x%base)
        x=x//base
    return(b)

def is_contained (source, term="."):
    return term in source

def point_split (x):
    L=x.split(".")
    return (L[0]), ("0." + L[1])

def BaseFormatter (x):
    dict = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
        20: "K",
        21: "L",
        22: "M",
        23: "N",
        24: "O",
        25: "P",
        26: "Q",
        27: "R",
        28: "S",
        29: "T",
        30: "U",
        31: "V",
        32: "W",
        33: "X",
        34: "Y",
        35: "Z"
    }
    L = []
    for i in x:
        if i != ".":
            if int(i) > 9:
                i = dict[int(i)]
        L.append(i)
    return L

def InverseBaseFormatter(x):
    dict =  {
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


def decimal_to_base(x,base=2):
    "base conversion of random floating points"
    x = str(x)
    if is_contained(x):
        intPart, decPart =  point_split(x)
        a = decimalint_to_binary(int(intPart),base) + point2Binary(float(decPart), base)
        a = BaseFormatter(a)
        return (a)
    else:
        a = decimalint_to_binary(int(x),base)
        a = BaseFormatter(a)
        return (a)

def int_n_2_B10 (x, base):
    x = InverseBaseFormatter(x)
    sum = 0
    for i,item in enumerate (x):
        sum += int(item) * base **(len(x)-1-i)
    return sum

def n_point_2_B10 (x, base):
    x = InverseBaseFormatter(str(x)[2:])
    sum = 0
    for i,item in enumerate (x):
        sum += int(item) * base ** -(i+1)
    return round(sum,len(x))

def n_2_B10 (x, base=2):
    x = str(x)
    if is_contained(x):
        intPart, decPart = point_split(x)
        return int_n_2_B10(intPart,base) + n_point_2_B10(decPart, base)
    else:
        return int_n_2_B10(x, base)

def base_n_to_base_n (v, from_b, to_b):
    v_to_10 = n_2_B10(v, from_b)
    if (to_b == 10):
        return v_to_10
    return decimal_to_base(v_to_10, to_b)



#for i in decimal_to_base(28394.68748,20):
 #   print(i, end="")

#print (n_2_B10("3AJE.DEJGF",20))

print(base_n_to_base_n("3AJE.DEJGF",20,16))