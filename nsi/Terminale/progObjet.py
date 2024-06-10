class Feu:
    '''La classe Feu permet de stocker
    la couleur du feu, Un objet de la
    classe Feu a un attribut couleur'''
    def __init__(self, c):
        self.couleur = c
    def change(self):
        if self.couleur=='vert':
            self.couleur='orange'
        elif self.couleur=='orange':
            self.couleur='rouge'
        else:
            self.couleur='vert'
feu1 = Feu('rouge')
feu2 = Feu('vert')


class Tps:
    """La classe tps pour noter le temps
    en heures, minutes et secondes"""
    def __init__(self, h, m, s):
        self.heu = h
        self.min = m
        self.sec = s

    def affiche(self):
        return str(self.heu)+" h "+str(self.min)+" m "+str(self.sec)+" s "
    def ajoute(self, s):
        self.sec += s
        #passage éventuel à la minute supérieure
        self.min += self.sec // 60
        self.sec = self.sec % 60
        #passage éventuel à l'heure supérieure
        self.heu += self.min // 60
        self.min = self.min % 60
        #passage éventuel au jour suivant
        self.heu = self.heu % 24

t1=Tps(11,20,55)
t2=Tps(14,45,12)

