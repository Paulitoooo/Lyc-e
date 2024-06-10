from random import randint

class Maillon:
    ''' Classe Maillon : chaque objet est défini par
    une valeur et le maillon suivant dans la liste'''
    def __init__(self, v, s):
        self.valeur = v
        self.suivant = s

def creerChaine(n):
    ''' Cette fonction crée une liste de chaînée de n éléments.
    Les valeurs sont des lettres aléatoires parmi A - B - C - D - E.
    L'étude de cette fonction n'est pas demandée. '''
    m = None
    for i in range(n):
        m = Maillon(chr(randint(65,70)),m)
    return m

tete = creerChaine(12) #Le premier maillon cette liste de 12 maillons a pour nom « tete ».

''' ************ votre code ici *************** '''

def Longueur(m):
        l = 1
        while m.suivant is not None:
            l = l + 1
            m = m.suivant
        return l

def afficheChaine(m):
        t = ''
        while m.suivant is not None:
            t=t+m.valeur
            m=m.suivant
        t=t+m.valeur
        return t
