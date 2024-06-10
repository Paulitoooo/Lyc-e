#s3:
#Exo1

class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.denom=d

    def __str__(self):
        if self.denom==1:
            return str(self.num)
        elif self.denom==0:
            return 'Erreur'
        else:
            return str(self.num)+'/'+str(self.denom)

    def simplif(self):
        for i in range(2, min(self.num,self.denom)):
            while self.num%i==0 and self.denom%i==0:
                self.num=self.num/i
                self.denom=self.denom/i
        return str(self.num) + "/" + str(self.denom)

fr=Fraction(128,32)

#Exo2:

class Angle:
    def __init__(self,d):
        self.angle=d

    def __str__(self):
        if self.angle>=360:
            return 'Erreur'
        elif self.angle<0:
            return 'Erreur'
        else :
            return str(self.angle)+'°'

    def ajoute(self,add):
        self.angle+=add
        if self.angle>=360:
            self.angle=self.angle-360
            return 'Erreur'
        elif self.angle<0:
            self.angle=self.angle+360

a1=Angle(90)