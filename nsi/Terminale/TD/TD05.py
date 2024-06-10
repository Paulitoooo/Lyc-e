#TD05 :

#Exo 3 :

class File:
    def __init__(self):
        self.taille=0
        self.contenu = []

    def enfile(self, e):
        self.taille=self.taille + 1
        self.contenu.append(e)

    def defile(self):
        if self.taille > 0:
            self.taille = self.taille - 1
            return self.contenu.pop(0)

    def __str__(self):
        cc=""
        t=self.taille
        for i in self.contenu:
            t=t-1
            cc = cc + str(i)
            if t>0:
                cc=cc+chr(8592)
        return cc

    def __len__(self):
        n=0
        for i in self.contenu:
            n=n+1
        return n

    def estVide(self):
        if len(self)==0:
            return True
        return False

    def lireTete(self):
        t=self.defile()
        self.enfile(t)
        n=self.taille-1
        for i in range(n):
            self.enfile(self.defile())
        return t

#Exo 4 :

from random import *

def alea(n):
    alea=File()
    for i in range(n):
        alea.enfile(randint(0,100))
    return alea

def gardepair(F):
    for i in range(len(F)):
        x = F.defile()
        if x%2==0:
            F.enfile(x)
    return F

def duplique(F):
    F2=File()
    for i in F.contenu:
        t=F.defile()
        F2.enfile(t)
        F.enfile(t)
    return F2

#Exo 6 :

class FileB:
    def __init__(self , n):
        self.elem= [None] * n
        self.capa = n
        self.nb = 0
    def est_vide(self):
        if self.nb == 0 :
            return True
        else:
            return False
    def est_pleine(self):
        if self.capa == self.nb:
            return True
        return False
    def enfiler(self,e):
        if not self.est_pleine():
            self.elem[self.nb]=e
            self.nb = self.nb + 1
        else:
            return 'File pleine'
    def defiler(self):
        if self.est_vide():
            return 'File vide'
        self.nb=self.nb-1
        e=self.elem[0]
        self.elem[0] = None
        return e
    def __str__(self):
        repo = ''
        for i in range(self.nb):
            repo = repo + '<' + str(self.elem[i])
        return repo

T1=File()
T1.enfile('A')
T1.enfile('B')
T1.enfile('C')

F1=alea(10)