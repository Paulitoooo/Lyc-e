#s9
class Noeud:
    #Noeud d'un arbre binaire
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d

def affiche(a):
    if a is None:
        return ''
    return '( '+affiche(a.gauche)+' '+str(a)+' '+affiche(a.droite)+' )'
#Exo 3:


def ajoute(x, arbre):
    if arbre is None:
        return Noeud(None,x,None)
    elif x < arbre.valeur:
        return Noeud(ajoute(x,arbre.gauche),arbre.valeur,arbre.droite)
    else:
        return Noeud(arbre.gauche,arbre.valeur,ajoute(x,arbre.droite))

arbre1= None

def minimum(a):
    if a is None:
        return None
    if a.gauche is None :
        return a.valeur
    else:
        return minimum(arbre.gauche)

def infixe(arbre):
    if arbre is None:
        return []
    return infixe(arbre.gauche)+[arbre.valeur]+infixe(arbre.droite)

from random import *
zat = [randint(0,100) for i in range(10)]
print(zat)
a = None
for i in zat:
    a = ajoute(i,a)
print(infixe(a))