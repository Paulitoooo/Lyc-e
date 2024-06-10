#Bac sujet C :

#Exo 1:
t=[4, 10, 0, 8]
def min_max(tab):
    dico={}
    dico['mini']=0
    dico['maxi']=0
    for i in tab:
        if i < dico['mini']:
            dico['mini']=i
        if i > dico['maxi'] :
            dico['maxi']=i
    return dico

#Exo 2

def fusion_rec(gauche,droite):
    if gauche==[] :
        return droite
    elif droite==[] :
        return gauche
    else :
        if gauche[0] <= droite[0]:
            return [gauche[0]]+fusion_rec(gauche[1:],droite)
        else :
            return [droite[0]]+fusion_rec(gauche,droite[1:])