#Exo 1 :
def puissance(x,n):
    c = 1
    for i in range(n):
        c = c * x
    return c

def puissanceR(x,n):
    if n == 1:
        return x
    if n == 0:
        return 1
    return x * puissanceR(x,n-1)

def factorielle(n):
    c = 1
    for i in range(n):
        c = c * n
        n=n-1
    return c

def factorielleR(n):
    if n == 1 or n == 0:
        return 1
    return n * factorielleR(n-1)

#Exo 2 :
def intervalle(i,k):
    print(i,end=" ")
    if i == k :
        return
    intervalle(i+1,k)

#Exo 4 :
from turtle import *


def koch(n,L):
    if n == 0:
        forward(L)
    else:
        koch(n-1,L/3)
        left(60)
        koch(n-1,L/3)
        right(120)
        koch(n-1,L/3)
        left(60)
        koch(n-1,L/3)
