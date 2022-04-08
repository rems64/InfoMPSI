import numpy as np
from matplotlib.pyplot import *

def Case(M,c):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if  M[i][j]==c:
                return (i,j)
    return False

"""
def Voisin(M):
    (i0, j0) = Case(M, 0)
    voisins = []
    if i0>0:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0-1][j0]
        voisins[-1][i0-1][j0] = 0
    if i0<2:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0+1][j0]
        voisins[-1][i0+1][j0] = 0
    if j0>0:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0][j0-1]
        voisins[-1][i0][j0-1] = 0
    if j0<2:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0][j0+1]
        voisins[-1][i0][j0+1] = 0
    return voisins
"""

def Voisin(M, sx, sy):
    (i0, j0) = Case(M, 0)
    voisins = []
    if i0>0:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0-1][j0]
        voisins[-1][i0-1][j0] = 0
    if i0<sx-1:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0+1][j0]
        voisins[-1][i0+1][j0] = 0
    if j0>0:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0][j0-1]
        voisins[-1][i0][j0-1] = 0
    if j0<sy-1:
        voisins.append(M.copy())
        voisins[-1][i0][j0] = voisins[-1][i0][j0+1]
        voisins[-1][i0][j0+1] = 0
    return voisins


def isIn(Q, Sphere):
    for s in Sphere:
        if np.all(s==Q):
            return True
    return False

def Hamming(P,Q):
    somme = 0
    for i in range(len(P)):
        for j in range(len(P[i])):
            if P[i,j]!=Q[i,j] and P[i,j]!=0:
                somme+=1
    return somme

def Manhattan(P,Q):
    somme = 0
    for i in range(len(P)):
        for j in range(len(P[i])):
            (k, l) = Case(Q, P[i, j])
            somme += abs(k-i)+abs(l-j)
    return somme

def Heuristiiiiiiiique(P,Q, alpha):
    return Manhattan(P,Q)+alpha*Hamming(P,Q)

def Resolution(I, F, alpha=3):
    Chemin = [I]
    DejaVus = [I]
    Test = True
    while Test and not np.all(Chemin[-1]==F):
        Test = False
        #Sphere = [k for k in Voisin(Chemin[-1]) if not isIn(k,DejaVus)]
        Sphere = []
        for k in Voisin(Chemin[-1], len(I), len(I[0])):
            if not isIn(k, DejaVus):
                Sphere.append(k)
        #print(Voisin(Chemins[-1]))
        #print(Sphere)
        if len(Sphere)>0:
            Test = True
            minDist = Heuristiiiiiiiique(Sphere[0], F, alpha)
            minEl = Sphere[0]
            for el in Sphere:
                d = Heuristiiiiiiiique(el, F, alpha)
                if d<minDist:
                    minDist = d
                    minEl = el
            Chemin+=[minEl]
            DejaVus+=[minEl]
        else:
            Chemin = Chemin[:-1]

    return Chemin
"""
def Resolution(I, F, alpha=3):
    Chemin = [I]
    DejaVus = [I]
    while not np.all(Chemin[-1]==F):
        #Sphere = [k for k in Voisin(Chemin[-1]) if not isIn(k,DejaVus)]
        Sphere = []
        for k in Voisin(Chemin[-1], len(I), len(I[0])):
            if not isIn(k, DejaVus):
                Sphere.append(k)
        #print(Voisin(Chemins[-1]))
        #print(Sphere)
        if len(Sphere)>0:
            minDist = Heuristiiiiiiiique(Sphere[0], F, alpha)
            minEl = Sphere[0]
            for el in Sphere:
                d = Heuristiiiiiiiique(el, F, alpha)
                if d<minDist:
                    minDist = d
                    minEl = el
            Chemin+=[minEl]
            DejaVus+=[minEl]
        else:
            Chemin = Chemin[:-1]

    return Chemin
"""

def Opti(I, F):
    chemin = Resolution(I,F)
    i=len(chemin)-1
    while i>0:
        voisin = Voisin()

def Animation(I, F):
    Chemin=Resolution (I, F, 3)
    print(len(Chemin))
    if Chemin != [] :
        i, c =0 ,0
        P=Chemin[i]
        ion()
        figure(1)
        axis("off")
        image=imshow(P, cmap="gray", interpolation="nearest")
        show()
        while i<len(Chemin):
            P=Chemin[i]
            image.set_data(P)
            title("Position après" + str(c) + "coups")
            axis("off")
            image.changed()
            draw()
            pause(0.001)
            c+=1
            i+=1
            show()

def Plot(I, F):
    x = np.linspace(-1,10,20)
    y=[]
    for i in x:
       y.append(len(Resolution(I,F,i)))
    figure(1)
    scatter(x,y)
    show()


#A=np.array([[6,4,7],[8,5,0],[3,2,1]])
#B=np.array([[1,2,3],[4,5,6],[7,8,0]])
#A = np.array([[8,13,14,6],[5,2,7,1],[12,3,9,11],[10,15,4,0]])
#B = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
#A = np.array([[15,2,10,1],[7,3,5,8],[12,9,11,14], [6,4,13,0]])
#B = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])
#c = Resolution(A, B)

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,0,12],[11,13,14,15]])
B = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
#print(c)
Animation(A,B)
#Plot(A,B)
