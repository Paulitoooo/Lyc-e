#TD01b
#Exo1

scrabble = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4,  'I':1,  'J':8,  'K':10,  'L':1,  'M':2,
            'N':1, 'O':1, 'P':3, 'Q':8, 'R':1, 'S':1, 'T':1, 'U':1,  'V':4,  'W':10,  'X':10,  'Y':10,  'Z':10}

codeVilar = {'A':'🜢', 'B':'🝥', 'C':'🜋', 'D':'🜩', 'E':'🜉', 'F':'🜞', 'G':'🝦', 'H':'🝓',  'I':'🝭',
            'J':'🝮', 'K':'🝘', 'L':'🜛', 'M':'🝂', 'N':'🝠', 'O':'🝣', 'P':'🜣', 'Q':'🜳', 'R':'🝐',
            'S':'🝰', 'T':'🜒', 'U':'🝆', 'V':'🜖', 'W':'🜤', 'X':'🜌', 'Y':'🜁', 'Z':'🜗', ' ':'🜼'}

desserts = {"Gâteau au chocolat": ["chocolat", "oeuf", "farine", "sucre", "beurre"]}
desserts["Gâteau au yaourt"] = ["yaourt", "oeuf", "farine", "sucre"]
desserts["Crêpes"] = ["oeuf", "farine", "lait"]
desserts["Quatre-quarts"] = ["oeuf", "farine", "beurre", "sucre"]
desserts["Kouign amann"] = ["farine", "beurre", "sucre"]


def valeurMot(m):
    v = 0
    tab = list(m)
    for i in tab:
        v=v+scrabble[i]
    return v

#Exo2

def lettres(t):
    l={}
    for i in t:
        if (i in l) is False:
            l[i]=1
        else:
            l[i]=l[i]+1
    return l

#Exo3

def code(t):
    c=''
    for i in t:
        if i in codeVilar:
            c=c+codeVilar[i]
        else:
            c=c+i
    return c


def decode(t):
    d=''
    for i in t:
        for j in codeVilar:
            if codeVilar[j] == i:
                d = d + j
    return d

#Exo4

def dessert(l):
    poss=[]
    for i in desserts.keys():
        reaB=True
        for j in desserts[i]:
            if j not in l:
                reaB=False
        if reaB:
            poss.append(i)
    return poss