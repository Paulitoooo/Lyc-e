#TD01
#Exo1

mesNotes = [10, 14, 8, 16, 15]

mesNotes.sort()
print(mesNotes)

mesNotes.sort(reverse=True)
print(mesNotes)

def maMoy(t):
    a=0
    b=len(t)
    for i in t:
        a=a+i
    return a/b

#Exo2
mesNotesCoef = [[10,2], [14,1], [8,2], [16,3], [15,2]]

def maMoyc(t):
    a=0
    b=0
    for i in t:
        b=b+i[1]
    for j in t:
        a=a+j[0]*j[1]
    return a/b

#Exo3:
tabPair=[i for i in range(0,101,2)]


#Exo4:
from random import *
tabAlea=[randint(0,100) for i in range(100)]

tab2=[j for j in tabAlea if j%3==0]

#Exo5:
monTab = ['Tim Berners-Lee', 'George Boole', 'John von Neumann', 'Alan Turing']
e=[]
f=[]
g=0
def nbCar():
    for i in monTab:
        e=list(i)
        g=len(e)
        f.append(g)
    return f

#Exo6:
Tab6=[[randint(0,9),randint(0,9),randint(0,9)] for i in range(20) ]
Tab6.sort(key=lambda x: x[1])

#Exo7:
monTuple = (10, 14, 12, 14)
a=monTuple[0]
b=monTuple[1]
c=monTuple[2]
d=monTuple[3]

monTuple2=(d,c,b,a)

def Moy(t):
    total=0
    denom=len(t)
    n=0
    for i in t:
        total=total+i
    return total/denom

def minmax():
    mini=monTuple[0]
    maxi=monTuple[0]
    for i in monTuple:
        if maxi<i:
            maxi=i
        if mini>i:
            mini=i
    MinMax=(mini,maxi)
#Exo8:
leTup=(5,)
L= ['rouge','vert','bleu']


#Exo9:
tup=()
for i in range(20):
    tB=(randint(0,10),)
    tup=tup+tB
print(tup)
print(tup.count(5))

#Exo10:
tup10=()
for i in range(100):
    tup2=(randint(1,6),randint(1,6),randint(1,6))
    tup10=tup10+(tup2,)
print(tup10)
for j in tup10:
    print(chr(9855+j[0]),chr(9855+j[1]),chr(9855+j[2]))

#Exo11:

Coul = [('blanc',[255,255,255]), ('saumon',[250,128,114]), ('vert',[0,128,0]),
('violet',[128,0,128]), ('turquoise',[64,224,208])]
Coul.sort(