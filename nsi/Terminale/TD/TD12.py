#TD12 :

#Exo 1:
from random import *

def alea(a,b):
    return [randint(0,b) for i in range(a)]

#Exo 2 :

L=alea(10,10)

def tri_insertion(T):
    for i in range(1,len(T)):
        temps=T[i]
        j=i
        while temps<T[j-1] and j>0:
            T[j]=T[j-1]
            j=j-1
        T[j] = temps
    return T

#Exo 3:

def tri_selection(T):
    for j in range(len(T)):
        mi=T[j]
        for i in range(j,len(T)):
            if T[i]<T[j]:
                r=T[j]
                T[j]=T[i]
                T[i]=r
                mi=T[i]
    return T