import math
import numpy as np


def getNext(v):
    if v[0]==0:
        if v[1]==1:return [[-1,0],False]
        return [[1,0],True]
    if v[0]==-1:return [[0,-1],False]
    return [[0,1],False]


def spirale(M):
    borne1 = [0, 0]
    borne2 = [M.shape[1]-1, M.shape[0]-1]
    index = 1
    position = [0,0]
    v = [1,0]
    while index < M.shape[0]*M.shape[1]:
        first = True
        while True:
            if not (position[0]==borne1[0] and position[1]==borne1[1]) or first:
                M[position[1],position[0]] = index
                first = False
            if position[0]+v[0]>borne2[0] : break
            if position[1]+v[1]>borne2[1] : break
            if position[0]+v[0]<borne1[0] : break
            if position[1]+v[1]<borne1[1] : break
            index+=1
            position[0]+=v[0]
            position[1]+=v[1]
        if getNext(v)[1]:
            borne1[0]+=1
            borne1[1]+=1
            borne2[0]-=1
            borne2[1]-=1
            position[0]+=1
            position[1]+=1
        v = getNext(v)[0]
    return M


tableau = np.zeros((20,12))


print(spirale(tableau))
