import pylab as plb
import math

def Harmonique(n):
    s=0
    for k in range(1,n+1):
       s+=(1/k)
    return s

def Seuil(s):
    n=0
    current = Harmonique(1)
    while current<s:
        n+=1
        current = Harmonique(n)
    return n

#print(Harmonique(10))
#print(Harmonique(50))
#print(Harmonique(100))


#print(Seuil(9))     # Prints 4550
#print(Seuil(9.1))   # Prints 5028



def Trace(n):
    plb.figure()
    plb.grid()
    xs=[x for x in range(n)]
    plb.title("Courbe polygonale $y=H(n)$")
    plb.plot(xs,[Harmonique(x) for x in xs],color="blue")
    M = plb.linspace(1,n,1000)
    plb.plot(M,[math.log(x) for x in M], color="red")
    plb.legend(('$ y=H(n)$','$y=\ln(x)$'),loc='upper left',shadow=True)
    plb.show()

Trace(100)
