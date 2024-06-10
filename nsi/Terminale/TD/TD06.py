#TD06 :
#Exo 1:

def remplir(L,n):
    for i in range(n,0,-1):
        L.append(i)
    return L

def remplir2(L,n):
    if n==0:
        return L
    else:
        L.append(n)
        return remplir2(L,n-1)

#2. Les deux listes sont identiques
#3. La fonction recursive , si n n'est pas égal à 0 , ajoute le nombre n (5 dans l'exemple) et
#   s'appelle elle même où elle ajoutera le nombre n-1 (4 puis 3 , 2 , 1) et a 0 elle renvoi L

#Exo 2:

def somme1(n):
    s=0
    for i in range(n+1):
        s = s + i
    return s

def somme2(n):
    if n==1:
        return n
    return n+somme2(n-1)

#Exo3 :

def mystere(a,b):
    if b==1:
        return a
    else:
        return a+mystere(a,b-1)

#Exo4 :
from turtle import *
def equi(a):
    forward(a)
    left(120)
    forward(a)
    left(120)
    forward(a)

def pointi(b):
    e=b/6
    c=0
    while c<b:
        forward(b/6)
        up()
        forward(e)
        down()
        c=c+b/6

#Exo5 :

from turtle import *

def dessine(n):
    if n>0:
        forward(n)
        right(90)
        dessine(n-5)


def libre(n):
    if n<0:
        return
    speed('fastest')
    hideturtle()
    equi(n)
    up()
    right(62)
    down()
    libre(n-2)

libre(400)