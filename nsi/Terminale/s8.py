class Noeud:
    #Noeud d'un arbre binaire
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d

Arbre = Noeud(None,'A',None)
Arbre.gauche=Noeud(None,'B',None)
Arbre.gauche.droite=Noeud(None,'D',None)
Arbre.droite=Noeud(None,'C',None)

def Affiche(MonArbre):
    if MonArbre is None:
        return
    print ("(", end=" ")
    Affiche(MonArbre.gauche)
    print (MonArbre.valeur, end=" ")
    Affiche(MonArbre.droite)
    print (")", end=" ")


Arbre9 = Noeud(None,27,Noeud(Noeud(None,9,Noeud(None,18,None)),36,None))

Arbre9B = Noeud(None,27,None)
Arbre9B.droite = Noeud(None,36,None)
Arbre9B.droite.gauche = Noeud(None,9,None)
Arbre9B.droite.gauche.droite = Noeud(None,18,None)


def Taille(MonArbre):
    if MonArbre is None:
        return 0
    else:
        return 1+Taille(MonArbre.gauche)+Taille(MonArbre.droite)


#Exo 7

sag = Noeud(Noeud(None,'D',None),'B',Noeud(Noeud(None,'H',None),'E',Noeud(None,'I',None)))
sad = Noeud(Noeud(None,'F',Noeud(None,'J',None)),'C',Noeud(None,'G',None))
arbre = Noeud(sag,'A',sad)

def infixe(a):
    if a is None:
        return ''
    return infixe(a.gauche) + a.valeur + infixe(a.droite)

def postfixe(a):
    if a is None:
        return ''
    return postfixe(a.gauche) + postfixe(a.droite) + a.valeur

def prefixe(a):
    if a is None:
        return ''
    return a.valeur + prefixe(a.gauche) + prefixe(a.droite)