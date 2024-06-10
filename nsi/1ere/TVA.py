def TTC(type,prix_HT):
    assert type<=2,"Le type de marchandise est soit de 1 ou 2"
    if type==1:
        return round(prix_HT*(1+10/100),2)
    else:
        return round(prix_HT*(1.2+10/100),2)