import math
from numpy import *

direction = [1,0]


def getNext(v):
    if v[0]==0:
        if v[1]==1:return [[-1,0],False]
        return [[1,0],True]
    if v[0]==-1:return [[0,-1],False]
    return [[0,1],False]


def spirale(M):
    borne1 = [0, 0]
    borne2 = [M.shape[0]-1, M.shape[1]-1]
    


tableau = zeros((5,5))

# print(getNext([1,0]))
# print(getNext([0,1]))
# print(getNext([-1,0]))
# print(getNext([0,-1]))

print(tableau)
print(spirale(tableau))
