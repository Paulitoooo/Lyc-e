#TD03:
class Maillon:
    def __init__(self,v,s=None):
        self.valeur=v
        self.suivant=s


class Chaine:
    def __init__(self):
        self.prem=None

    def __str__(self):
        aff= ""
        maillonFocus = self.prem
        while maillonFocus is not None :
            aff=aff + maillonFocus.valeur + " "
            maillonFocus = maillonFocus.suivant
        return aff

    def __len__(self):
        l=0
        maillonFocus=self.prem
        while maillonFocus is not None :
            l=l+1
            maillonFocus=maillonFocus.suivant
        return l

    def afficheMaillon(self,i):
        if i<0 or i>=len(self):
            return None
        maillonFocus=self.prem
        for i in range(i):
            maillonFocus=maillonFocus.suivant
        return maillonFocus.valeur

    def reverse(ch):
        newChaine = Chaine()
        newChaine.prem = Maillon(ch.AfficheMaillon(len(ch)-1,None))
        maillonW = newChaine.prem
        for i in range(len(ch)-2,-1,-1):
            maillonW.suivant = Maillon(ch.AfficheMaillon(i),None)
            maillonW=maillonW.suivant
        return newChaine

    def concatenation(ch1,ch2):
        newChaine = Chaine()
        newChaine.prem.valeur = ch1.prem.valeur
        maillonW = newChaine.prem
        for i in range(1,len(ch1)):
            maillonW.suivant = Maillon(ch1.afficheMaillon(i),None)
            maillonW = maillonW.suivant


liste1=Chaine()
liste1.prem = Maillon('N',Maillon('S',Maillon('I',)))