import math
import pylab as plb

globalCount=0

def fonction1(x):
    return 2*x+2

def fonction2(x):
    return 2*x * math.e**x - 1

def fonction3(x):
    return 0.5**x - 1E-10

def fonction4(x):
    return x**2-2

def Dichotomie(F,a,b,erreur):
    global globalCount
    if(abs(b-a)<erreur):
        return [a,b]
    globalCount+=1

    m=(a+b)/2
    if(F(a)*F(m)<0):
        b = m
    else:
        a = m

    return Dichotomie(F,a, b, erreur)

def Trace(a, b):
    plb.figure()
    plb.grid()
    M = plb.linspace(a, b, 1000)
    plb.plot(M,[fonction2(x) for x in M], color="red")
    plb.legend(('$ y=H(n)$','$y=\ln(x)$'),loc='upper left',shadow=True)
    plb.show()


#bornes = Dichotomie(fonction3, 20, 50, 1E-8)
bornes = Dichotomie(fonction4, 0, 2, 1E-10)
print(bornes)
print(globalCount)
Trace(bornes[0], bornes[1])
