#TD00
#Exo 1
Phrase1 = "Julie vend quatre ceintures"
Phrase2 = "Vladimir aime follement repartir nager"

def decode(phrase):
   tab = phrase.split()
   R = [tab[i][i] for i in range(len(tab))]
   return R

#Exo 2

location=[['audi', 'Q5', 'noire', 'BG 578 ZM', 25041],
         ['peugeot', '206', 'rouge', 'CF 431 FT', 5205],
         ['ferrari', 'turismo', 'noire', 'JF 409 KL', 17980]]

def km(plaque,distance):
    for i in location:
        if plaque==i[3]:
            i[4]=i[4]+distance
            return 'validé'
    return 'erreur'

def ajout(marque,modele,couleur,plaque,compteur):
    tab=[marque,modele,couleur,plaque,compteur]
    location.append(tab)
    return "ajout validé , saisissez 'location' pour voir la liste"

def tri(liste):
    return sorted(liste,key=lambda x: x[4])