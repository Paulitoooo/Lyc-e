def creer_file():
    return []

def ajouter_file(f,x):
    f.append(x)
    return f

def retirer_file(f):
    if len(f)>0:
        return f.pop(0)
    return None

maFile=creer_file()

#Exercice 3 :

def creer_fileb(n):
    return [0] + n * [None]

def enfilerb(f,x):
    if f[-1] is None:
        f[f[0]+1]=x
        f[0] = f[0] + 1
    else:
        return 'Erreur'

def defilerb(f):
    f.pop(1)
    f[0]=f[0]-1
    f.append(None)

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
        for i in self.contenu:
            cc = cc + str(i) + chr(8592)
        return cc

T1=  File()
T1.enfile('A')
T1.enfile('B')
T1.enfile('C')

def retourne(f):
    Q=creer_file()



Fb1=creer_fileb(5)
enfilerb(Fb1,3)
enfilerb(Fb1,4)

def creer_fileC(n):
    return [0,0] + n*[None]

def enfilerC(f,x):
    if f[0] == 0 :
        #la liste est vide
        f[0] = 2
        f[1] = 2
        f[2] = x
    else:
        #file non vide
        #est-ce qu'il y a la place nécessaire ?
        if f[1]+1==f[0]:
            return 'File pleine'
        if f[1] == len(f)-1 and f[0]==2:
            return 'File pleine'
        f[1] = f[1] + 1
        if f[1]>=len(f):
            f[1] = 2
        f[f[1]] = x

def defilerC(f):
    if f[0]==0:
        return 'file vide'
    x = f[f[0]]
    f[f[0]]=None
    f[0] = f[0] + 1
    if f[0]>=len(f):
        f[0]=2
    return x

F1= creer_fileC(3)
enfilerC(F1,78)
enfilerC(F1,45)
enfilerC(F1,89)