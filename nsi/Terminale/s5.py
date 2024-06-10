def creer_pile():
    # renvoie une pile vide
    return []
def empiler(p,x):
    # ajoute x à la pile p
    p.append(x)
def depiler(p):
    # renvoie le sommet de la pile
    # si elle n'est pas vide
    # Ce sommet est retiré de la pile.
    if len(p) > 0:
        return p.pop()

def pilevide(p):
    if p==[]:
        return True
    else:
        return False

def taille(p):
    new_pile=creer_pile()
    C = 0
    while not pilevide(p):
        empiler(new_pile,depiler(p))
        C = C + 1
    while not pilevide(new_pile):
        empiler(p,depiler(new_pile))
    return C

def sommet(p):
    if p==[]:
        return 'rien'
    else:
        return p[taille(p)-1]

def creer_pileB(c):
    p=[]
    p.append(0)
    for i in range(c):
        p.append(None)
    return p

def empilerB(p,x):
    if p[-1] == None:
        p[p[0]+1]= x

def deplier(p):
    if p[0]>0:
        A = p[p[0]]
        p[p[0]] = None
        p[0]=p[0]-1
        return A

def ViderB(p):
    for i in range(p[0]):
        deplier(p)

#def InverseB(p):
    #pile_temp = creer_pileB(

def hauteur_pile(P):
    Q=creer_pile()
    n=0
    while not(pilevide(P)):
        n=n+1
        x=depiler(P)
        empiler(Q,x)
    while not(pilevide(Q)):
        x=depiler(Q)
        empiler(P,x)
    return n

def max_pile(P,i):
    Q=creer_pile()
    n=0
    while not(pilevide(P)):
        x=depiler(P)
        if x==i:
            n=n+1
        empiler(Q,x)
    while not(pilevide(Q)):
        x=depiler(Q)
        empiler(P,x)
    return n

def retourner(P,j):
    Q=creer_pile()
    R=creer_pile()
    while j>0:
        j=j-1
        x=depiler(P)
        empiler(Q,x)
    while not(pilevide(Q)):
        x=depiler(Q)
        empiler(R,x)
    while not(pilevide(R)):
        x=depiler(R)
        empiler(P,x)
    return P

P=[8,5,2,4]

PileB=creer_pileB(4)

Pile1=creer_pile()
empiler(Pile1,'V')
empiler(Pile1,'I')
empiler(Pile1,'L')
empiler(Pile1,'A')
empiler(Pile1,'R')

Pile2 = creer_pile()
empiler(Pile2, depiler(Pile1))
empiler(Pile2, depiler(Pile1))
depiler(Pile1)
empiler(Pile2, depiler(Pile1))
Pile3 = creer_pile()
while Pile2 != []:
 empiler(Pile3, depiler(Pile2))
while Pile3 != []:
 empiler(Pile1, depiler(Pile3))
print(Pile1)