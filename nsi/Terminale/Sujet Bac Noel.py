#Sujet bac Noel :

#Sujet B:

def multiple(tab,n):
    c=0
    for i in tab:
        if i%n==0:
            c=c+1
    return c

#Sujet D:

def recherche(tab):
    l=[]
    for i in range(len(tab)-1):
        n=i+1
        if tab[i]-tab[n]==-1:
            t=tuple((tab[i],tab[n]))
            l.append(t)
    return l