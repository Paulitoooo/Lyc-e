
#TD04 :
#Exo 1 :

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

#Exo 2:

def creerPileB(c):
    p = [0] + c * [None]
    return p

def empilerB(p, e):
    if p[-1] == None:
        p[p[0]+1]= e
        p[0]=p[0]+1
    else:
        return 'Impossible , la pile est pleine'

def depilerB(p):
    if p[0]>0:
        A = p[p[0]]
        p[p[0]] = None
        p[0]=p[0]-1
        return A

def sommetB(p):
    if p[0]==0:
        return 'rien'
    else:
        return p[p[0]]

def tailleB(p):
    return p[0]

Pb1=creerPileB(2)
empilerB(Pb1,'A')

pB=creerPileB(5)
empilerB(pB,'A')
empilerB(pB,'B')
empilerB(pB,'C')
empilerB(pB,'D')

def viderPileB(p):
    for i in range(p[0]):
        depilerB(p)

def inverserPileB(p):
    x=p[0]
    new_pile=creerPileB(x)
    for i in range(x):
        empilerB(new_pile,p[x])
        x=x-1
    return new_pile

#Exo 3 :

class Pile:
    def __init__(self):
        self.elem=[]

    def est_vide(self):
        if self.elem==[]:
            return True
        return False

    def empiler(self, e):
        self.elem=self.elem+[e]

    def depiler(self):
        self.elem=self.elem-self.elem[-1]

P1=Pile()
P1.empiler('A')

#def entendre(pile1,pile2):
    #nb_element=pile2.nb_elements()
    #for i in range(nb_element):
     #   e=pile2.depiler()
      #  pile1.empiler(e)
    #return pile1

#def supp(pile,element):
    #for i in pile:
     #   if i==element

#Exo 5:

def calcule(l):
    l2=Pile()
    oper= ("+","-","*","/")
    R = 0
    for i in oper:
        e1=pile.depiler()
        e2=pile.depiler()
        Pile.empiler(eval(str(e2)+i+str(e1)))
