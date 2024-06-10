#s15 :

class Pile:
    def __init__(self):
        self.elem=[]

    def empile(self,d):
        self.elem.append(d)

    def depile(self):
        return self.elem.pop(-1)

    def sommet(self):
        return self.elem[-1]

    def hauteur(self):
        return len(self.elem)

def affiche(p1,p2,p3):
    tours = (p1,p2,p3)
    h = 0
    for i in range(3):
        if tours[i].hauteur() > h:
            h = tours[i].hauteur()
    for i in range(h-1,-1,-1):
        for j in range(3):
            if tours[j].hauteur() > i:
                print('(',tours[j].elem[i],')',end=" ")
            else:
                print(' ',end=" ")
        print()
    print('---------------------')

P=Pile()
P.empile(5)

def depart(n):
    p=Pile()
    for i in range(n,0,-1):
        p.empile(i)
    return p

def obj(nPile):
    if nPile == 1 :
        return p1
    elif nPile == 2 :
        return p2
    elif nPile == 3 :
        return p3


n=int(input("Nombre de disques ? "))
p1=depart(n)
p2=depart(0)
p3=depart(0)
affiche(p1,p2,p3)

def deplace(d,a,i,k):
    if k>0:
        deplace(d,i,a,k-1)
        a.empile(d.depile)
        affiche(p1,p2,p3)
        deplace(i,a,d,k-1)