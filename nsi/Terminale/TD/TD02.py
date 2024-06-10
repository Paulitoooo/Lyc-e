#TD02 :
#Exo1 :

class Livre:
    '''Le livre a 2 attributs : auteur et prix'''
    def __init__(self,a,p):
        self.auteur=a
        self.prix=p

    def adherent(self):
        '''Renvoie le prix adhérent avec une remise de 10%
        Le prix est arrondit au centime près'''
        return self.prix-self.prix/10

Germinal=Livre('Zola',15.5)
Les_miserables=Livre('Hugo',18.3)

#Exo2 :

class Rectangle:
    def __init__(self,la,lo):
        self.larg=la
        self.long=lo

    def perimetre(self):
        return self.larg*2+self.long*2

    def aire(self):
        return self.larg*self.long

rect1=Rectangle(6,9)
rect2=Rectangle(3,18)

#Exo3 :

class Voiture:
    def __init__(self,ma,mo,color,comp):
        self.marque=ma
        self.modele=mo
        self.couleur=color
        self.compteur=comp

    def roule(self,dist):
        self.compteur=self.compteur+dist

V1= Voiture('Ferrari','F40','rouge',15400)
V2= Voiture('Porsche','911','noire',36515)
V3= Voiture('Lamborghini','Aventador','jaune',4012)

#Exo4:

from datetime import datetime
j = datetime.now().day
m = datetime.now().month
a = datetime.now().year

class Individu:
    def __init__(self,jo,mo,an,t):
        self.jNaiss=jo
        self.mNaiss=mo
        self.aNaiss=an
        self.taille=t

    def __str__(X):
        return 'Cette personne est née le '+str(X.jNaiss)+'/'+str(X.mNaiss)+'/'+str(X.aNaiss)

    def grandir(self,h):
        self.taille=self.taille+h

    def age(self):
        ag=a-self.aNaiss-1
        if m>=self.mNaiss:
            if j>=self.jNaiss:
                ag=ag+1
        return ag

Raoul=Individu(21,12,2000,183)
Luc=Individu(30,9,1993,172)
Max=Individu(5,3,2004,168)

#Exo5 :

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v
    def getNom(self):
        """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
    def getCouleur(self):
        if self.Couleur==0:
            return 'pique'
        elif self.Couleur==1:
            return 'coeur'
        elif self.Couleur==2:
            return 'carreau'
        else:
            return 'trefle'

    def __str__(self):
        return str(self.getNom())+' de '+str(self.getCouleur())

C1=Carte(3,12)
C2=Carte(1,11)

#Exo6 :

class PaquetDeCartes:
    def __init__(self):
        self.contenu=[]

    def remplir(self):
        for i in range(0,4):
            for j in range(1,14):
                self.contenu=self.contenu+[Carte(i,j)]

    def getCarte(self,p):
        return P1[p][1]+' de '+P1[p][0]

P1=PaquetDeCartes()