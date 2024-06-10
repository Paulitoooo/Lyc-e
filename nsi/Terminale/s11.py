#s11

from random import *
Liste=[randint(0,50) for i in range(30)]

def fusion(a, b):
    l = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            l.append(a.pop(0))
        else:
            l.append(b.pop(0))
    if len(a) > 0:
        l = l + a
    if len(b) > 0:
        l = l + b
    return l

def trifusion(L):
    if len(L)<2:
        return L
    else:
        milieu=len(L)//2
        L1=trifusion(L[:milieu])
        L2=trifusion(L[milieu:])
        return fusion(L1,L2)

def trifusionI(L):
    l = [[i] for i in L]
    l2=[]
    while len(l)>1:
        j = 0
        while j+1<len(l):
            l[j]= fusion(l[j],l[j+1])
            l.pop(j+1)
            j=j+1
    return l