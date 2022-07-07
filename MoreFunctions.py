def VariableParameter (*Pars): #we use '*' generallly to mean any
    for i in Pars:
        print(i,end=",")
    print()

"""
VariableParameter()
VariableParameter(1)
VariableParameter(1,2)
VariableParameter(1,2,3)

"""


def mean (*num):
    sum = 0
    for i in num:
        sum +=i
    if len(num) == 0:
        print("You can't compute a mean of an empty collection")
    else:
        print ("The mean is: " + str(sum/len(num)))

# mean(1,2,3,4,5,567,4,68,5,5,7,76,878,23)

def harmonic_mean (*num):
    ReciprocalSum = 0
    for i in num:
        ReciprocalSum += 1/i
    if len(num) == 0:
        print("You can't compute a mean of an empty collection")
    else:
        print ("The harmonic mean is: " + str(len(num)/ReciprocalSum))

# harmonic_mean(1,2,3,4,5,567,4,68,5,5,7,76,878,23)

def f (**Parms):
    SN = 0
    SD = 0
    for key in Parms.keys():
        if (str(key)[0]=="N"):
            SN += Parms[key]
        else:
            SD += Parms[key]
    return (SN/SD)
/
print(f(N1=2,N2=3,N3=4,N4=5,D1=3,D2=5,D3=8,D4=9))
