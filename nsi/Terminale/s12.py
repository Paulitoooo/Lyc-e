#S12 :

L=[1,2,3,5,7,11,13]

from math import *

def Rechercher(a,T):
    prem = 0
    der = T[-1]
    while prem < der :
        milieu = floor((prem + der) / 2)
        if a == T[milieu] :
            return True
        else:
            if a > T[milieu] :
                prem = milieu + 1
            else :
                der = milieu - 1
    return False

from random import *

def montab():
    t = [randint(0,20) for i in range(15)]
    t.sort()
    return t

T = montab()

def Rechercher2(a,T):
    if len(T)==0:
        return False
    milieu = len(T) // 2