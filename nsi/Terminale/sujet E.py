#Sujet E :

#Exo 1 :

def taille(a,s):
    if a[s] == (None, None) :
        return 1
    if a[s][0] is None:
        return 1 + taille(a,a[s][1])
    elif a[s][1] is None:
        return 1 + taille(a,a[s][0])
    else:
        return 1 + taille(a,a[s][0]) + taille(a,a[s][1])