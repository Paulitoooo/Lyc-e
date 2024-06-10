anim = [('Lion', 750, 45),('Gnou', 670, 36),('Tigre', 375, 27),('Ours', 600, 54)]

def maxi(chrono):
    vit=0
    rapide=''
    for i in chrono:
        v = i[1]/i[2]
        if v > vit:
            vit = v
            rapide = i[0]
    return rapide

print(maxi(anim))

def rendu_monnaie(somme, pieces):
    n = len(pieces)
    rendre = []
    for i in range(n - 1, -1, -1):
        while somme >= pieces[i]
            somme = somme - pieces[i]
            rendre.append(pieces[i])
    assert somme == 0 , 'Pas assez de pièces dans le monnayeur'
    return rendre