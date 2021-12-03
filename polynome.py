import random
import numpy as np

class Polynome():
    def __init__(self, liste=[], size=0):
        if size==0:
            self.poly = liste
        else:
            self.poly = [0 for k in range(size)]

    def setN(self, index, set):
        self.poly[index] = int(not not set)

    def length(self):
        return len(self.poly)

    def eval(self, a):
        somme = 0
        for i in range(len(self.poly)):
            somme+=self.poly[i]*(a)**i
        return somme

    def degre(self):
        for k in range(1, len(self.poly)+1):
            if self.poly[len(self.poly)-k]:
                return k
        return 0

    def __str__(self):
        chaine = ""
        i=0
        for k in self.poly:
            #chaine+=str(k)+"(-2)^"+str(i)+(" + " if i<len(self.poly)-1 else "")
            chaine+="(-2)^"+str(i)+(" + " if i<len(self.poly)-1 else "") if k else ""
            i+=1
        return chaine

    def __repr__(self):
        return str(self.poly)

    def __getitem__(self, key):
        return self.poly[key]

    def __le__(self, P2):
        for i in range(min(self.length(), P2.length())):
            if self.poly[i]<P2[i] : return True
            if self.poly[i]>P2[i] : return False
        return self.length()<=P2.length()

    def __lt__(self, P2):
        for i in range(min(self.length(), P2.length())):
            if self.poly[i]<P2[i] : return True
            if self.poly[i]>P2[i] : return False
        return self.length()<P2.length()


def Degre(n):
    poly = []
    for i in range(2**n):
        #poly1 = [int(k) for k in bin(i)[2:]]
        #poly1 = [int(bin(i)[2:][k]) if k < len(bin(i)[2:]) else 0 for k in range(n)]
        #poly1 = [int(i & (1 << j)==0) for j in range(n)]
        poly1 = Polynome(size=n)
        for j in range(n):
            poly1.setN(j, int(i & (1 << j)==0))
        #print(poly1.degre())
        #if poly1.degre()==n:
            #print("valide")
        poly.append(poly1)
    return poly

def Degre_inf(n):
    polynomes = []
    for i in range(n):
        for j in Degre(i+1):
            polynomes.append(j)
    return polynomes


def Tri(n):
    liste = Degre_inf(n)
    M=[]
    for i in range(len(liste)):
        M.append(min(liste))
        liste.remove(min(liste))
    return M

def selectSort(L):
    sortedList = []
    temp = L.copy()
    for i in range(len(L)):
        sortedList.append(min(temp))
        temp.remove(min(temp))
    return sortedList

def Eval(n):
    liste = []
    for P in Tri(n):
        print(P)
        liste.append(P.eval(-2))
    return liste

def Find(a):
    found = False
    deg = 1
    while 1:
        polynomes = Degre(deg)
        for poly in polynomes:
            if poly.eval(-2)==a:
                return poly
        deg+=1

l1 = [0, 1, 1, 1, 1]
l2 = [1, 1, 0]

p1 = Polynome(l1)
p2 = Polynome(l2)

print(Find(833))

#print(Degre(4))

#print(Eval(4))
