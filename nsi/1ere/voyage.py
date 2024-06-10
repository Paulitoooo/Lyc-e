def vitesse(d,t):
    assert t!=0,"On ne peut pas diviser pas zéro"
    assert type(t) is not str,"On ne peut pas diviser par du texte"
    assert type(d) is not str,"Un texte ne peut pas etre divisé"
    assert t>0,"t ne doit pas etre négatif"
    assert d>0,"d ne doit pas etre négatif"
    v=d/t
    v=v*60
    return v

def distance(v,t):
    assert type(t) is not str,"On ne peut pas multiplier par du texte"
    assert type(v) is not str,"Un texte ne peut pas etre multiplier"
    assert v>0,"v ne doit pas etre négatif"
    assert t>0,"t ne doit pas etre négatif"
    t=t/60
    return v*t

def duree(v,d):
    assert v!=0,"On ne peut pas diviser par zéro"
    assert type(v) is not str,"on ne peut pas diviser par du texte"
    assert type(d) is not str,"on ne peut pas diviser par du texte"
    return d/v