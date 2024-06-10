class Pile:
    def __init__(self):
        self.elem=[]
    def empile(self,v):
        self.elem.append(v)
    def depile(self):
        return self.elem.pop(-1)
    def sommet(self):
        if self.hauteur() > 0:
            return self.elem[-1]
        else:
            return 0
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
                print('     ',end=" ")
        print()
    print('---------------------')

def depart(n):
    ''' Permet de créer une pile de n éléments '''
    P = Pile()
    for i in range(n,0,-1):
        P.empile(i)
    return P