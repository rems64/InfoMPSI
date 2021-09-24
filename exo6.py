from pylab import *

def Diffusion(M) :
    c=0
    P=M.copy()
    ion()
    figure(1)
    axis('off')
    image=imshow(P,cmap="gray",interpolation="nearest")
    show()
    pause(0.1)
    while fignum_exists(1)  :
        P=Successeur(P)
        image.set_data(P)
        title("Diffusion après "+str(c)+" étapes.")
        axis('off')
        image.changed()
        draw()
        pause(0.01)
        c+=1
        show()
    ioff()

##############################################

def Canon() :
    n=50
    M=ones((n,n))
    M[15,10]=0
    M[16,10]=0
    M[15,11]=0
    M[16,11]=0
    M[15,20]=0
    M[16,20]=0
    M[17,20]=0
    M[14,21]=0
    M[18,21]=0
    M[13,22]=0
    M[19,22]=0
    M[13,23]=0
    M[19,23]=0
    M[16,24]=0
    M[14,25]=0
    M[18,25]=0
    M[15,26]=0
    M[16,26]=0
    M[17,26]=0
    M[16,27]=0
    M[13,30]=0
    M[14,30]=0
    M[15,30]=0
    M[13,31]=0
    M[14,31]=0
    M[15,31]=0
    M[12,32]=0
    M[16,32]=0
    M[11,34]=0
    M[12,34]=0
    M[16,34]=0
    M[17,34]=0
    M[13,44]=0
    M[14,44]=0
    M[13,45]=0
    M[14,45]=0
    return M


def oscillateur():
    n=10
    M = ones((n, n))
    M[5, 3]=0
    M[5, 4]=0
    M[5, 5]=0
    return M

###############################

def Alea(p, n=40):
    #n=40
    M=ones((n,n))
    for i in range(n) :
        for j in range(n) :
            M[i,j]=binomial(1,1-p)
    return M






###############################

def Voisins(case, n):
    voisins = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if case[0]+i<0 or case[1]+j<0:
                continue
            if case[0]+i>n-1 or case[1]+j>n-1:
                continue
            voisins.append([case[0]+i, case[1]+j])
    return voisins


#print(Voisins([3,5],10))

def Successeur(M):
    cote = M.shape[0]
    newM = M.copy()
    for i in range(cote):
        for j in range(cote):
            voisins = Voisins([i, j], cote)
            sommeVoisins = 0
            for elem in voisins:
                if not M[elem[0],elem[1]]:
                    sommeVoisins+=1

            if M[i, j]==0:
                if not (sommeVoisins==2 or sommeVoisins==3):
                    newM[i,j] = 1
            else:
                if sommeVoisins==3:
                    newM[i, j] = 0
    return newM

#Diffusion(Alea(0.3,60))
Diffusion(Canon())
