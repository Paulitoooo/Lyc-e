#Sujet BAC J :

#Exo 1 :
def bin_dec(b):
    entier=0
    b.reverse()
    for i in range(len(b)):
        if b[i]==1:
            entier = entier + 2**i
    return entier

#Exo 2 :

def dichotomie(tab, x):
    debut = 0
    fin = len(tab)
    while debut <= fin :
        milieu = debut+fin//2
        if tab[milieu] == x:
            return True
        elif tab[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu
    return False