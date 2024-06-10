from hanoi1 import *
def obj(nPile):
    if nPile == 1:
        return p1
    elif nPile == 2:
        return p2
    elif nPile == 3:
        return p3

n = int(input("Nombre de disques ? "))
p1 = depart(n)
p2 = depart(0)
p3 = depart(0)
affiche(p1,p2,p3)
nd=0
while p3.hauteur()<n:
    d = obj(int(input('depart → ')))
    a = obj(int(input('arrivée → ')))
    if d.hauteur() == 0:
        print('départ vide')
    elif a.hauteur()!=0 and a.sommet() < d.sommet():
        print('déplacement interdit')
    else:
        nd = nd + 1
        a.empile(d.depile())
    affiche(p1,p2,p3)
print("Bravo en "+str(nd)+" déplacements")