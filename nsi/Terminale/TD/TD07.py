#TD07:
#Exo 2:

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], \
'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}


def taille(Ab,s):
    if s not in Ab:
        return 0
    sag = Ab[s][0]
    sad = Ab[s][1]
    if sag=='' and sad=='':
        return 1
    if sag !='' and sad=='':
        return 1 + taille(Ab,sag)
    if sag == '' and sad!='':
        return 1 + taille(Ab,sad)
    return 1 + taille(Ab,sag) + taille(Ab,sad)

#Exo 3:

a3 = ['A',['B',['D'],['E']],['C',['F'],[]]]

#Exo 4:

    #1 . Taille 5 hauteur 4

    #2.1 . G = 1010
    #2.2 .

#Exo 5:

class Noeud:
    def __init__(self ,valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def __str__(self):
        return str(self.valeur)

def affiche(a):
    if a is None:
        return ''
    return '( '+affiche(a.gauche)+' '+str(a)+' '+affiche(a.droit)+' )'

def tailleArbre(a):
    if a is None:
        return 0
    return 1 + tailleArbre(a.gauche) + tailleArbre(a.droit)

def hauteur(a):
    if a is None:
        return 0
    return 1+max(hauteur(a.gauche),hauteur(a.droit))

def feuille(a):
    if a.gauche is None and a.droit is None:
        return 1
    return feuille(a.gauche) + feuille(a.droit)

def cherche(a,x):
    if a is None :
        return 0
    if a.valeur == x:
        return 1+cherche(a.gauche,x)+cherche(a.droit)

Arbre5 = Noeud(1)
Arbre5.gauche = Noeud(2)
Arbre5.gauche.gauche = Noeud(3)
Arbre5.gauche.gauche.gauche = Noeud(7)
Arbre5.gauche.gauche.droit = Noeud(4)
Arbre5.gauche.droit = Noeud(5)
Arbre5.gauche.droit.gauche = Noeud(3)
Arbre5.droit = Noeud(3)
Arbre5.droit.gauche = Noeud(6)
Arbre5.droit.gauche.gauche = Noeud(5)
