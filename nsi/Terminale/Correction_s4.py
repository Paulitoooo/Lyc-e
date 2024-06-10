class Maillon :
    def __init__(self, v, s):
        self.valeur = v
        self.suivant = s

class Chaine:
    def __init__(self):
        self.tete = None
    def ajoute(self, e) :
        self.tete = Maillon(e, self.tete)
    def __str__(self):
        m = self.tete
        c = ''
        while m is not None:
            c = c + m.valeur
            m = m.suivant
        return c
    def __len__(self):
        m = self.tete
        n = 0
        while m is not None:
            n = n + 1
            m = m.suivant
        return n
    def vide(self):
        if self.tete is None:
            return True
        return False
    def supprime(self, i):
        if not self.vide():
            if i == 0:
                self.tete = self.tete.suivant
            else:
                m = self.tete
                n = 0
                while m is not None:
                    if i == n + 1:
                        m.suivant = m.suivant.suivant
                    n = n + 1
                    m = m.suivant
    def insere(self, i, v):
        if i==0:
            self.tete=Maillon(v,self.tete)
        elif i > 0 and i < len(self):
            m = self.tete
            for i in range(i):
                p = m
                m = m.suivant
            n = Maillon(v,m)
            p.suivant = n

C1 = Chaine()
C1.ajoute('T')
C1.ajoute('U')
C1.ajoute('A')
C1.ajoute('S')
