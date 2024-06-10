class Maillon :
    def __init__(self, v, s):
        self.valeur = v
        self.suivant = s


    def Longueur(maill):
        l = 1
        while maill.suivant is not None:
            l = l + 1
            maill = maill.suivant
        return l

    def affiche(maill):
        t = ''
        while maill.suivant is not None:
            t=t+maill.valeur
            maill=maill.suivant
        t=t+maill.valeur
        return t

maillon1=Maillon('Le',None)
maillon1.suivant=Maillon('Lycée',None)
maillon1.suivant.suivant=Maillon('Jean',None)
maillon1.suivant.suivant.suivant=Maillon('Vilar',None)

class Chaine:
    def __init__(self):
        self.tete = None

    def __len__(self):
        C=0
        maill = self.tete
        while maill is not None:
            maill=maill.suivant
            C+C+1
        return C

    def __str__(self):
        ch=""
        maill=self.tete
        while maill is not None:
            maill=maill.suivant
            ch=ch+maill
        return ch

    def estVide(self):
        if len(self)==0:
            return True
        else:
            return False

    def ajoute(self, e) :
        self.tete = Maillon(e, self.tete)

    def supprime(n,self):
        if n==0 and self.tete is not None:
            self.tete=self.tete.suivant
        if n>0:
            maill = self.tete
            for j in range(i-1):
                maill=maill.suivant
            maill.suivant=maill.suivant.suivant

    def insere(self,i,v):
        if i==0:
            self.ajoute(v)
        else:
            maill = self.tete
            for j in range(i-1):
                maill=maill.suivant
            maill.suivant=Maillon(v,maill.suivant.suivant)


C1=Chaine()
C1.ajoute('T')
C1.ajoute('U')
C1.ajoute('A')
C1.ajoute('S')