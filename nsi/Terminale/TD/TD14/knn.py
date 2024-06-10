from pylab import *

def lecture(fichier):
    fichier = 'C:/Users/Gresset Paul/Documents/0-Tale/NSI/TD/TD14/'+fichier
    f=open(fichier, encoding="UTF-8")
    LeTexte=f.read()
    f.close()
    return LeTexte

def frequence(T):
    nu = 0
    nh = 0
    T = T.lower()
    for i in T:
        if i == 'u': nu = nu + 1
        if i == 'h': nh = nh + 1
    return (100*nu/len(T),100*nh/len(T))

def totale():
    L = []
    for i in range(10):
        nf = "F"+str(i)+".txt"
        tup = frequence(lecture(nf))+("F",)
        L.append(tup)
        nf = "A"+str(i)+".txt"
        tup = frequence(lecture(nf))+("A",)
        L.append(tup)
    return L

LT = totale()

for i in LT:
    if i[2]=='A':
        col = 'red'
    else:
        col = 'blue'
    scatter(i[0],i[1],c=col)

show(block = False)
