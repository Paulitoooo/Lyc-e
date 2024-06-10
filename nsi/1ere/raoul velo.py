def distance(n):
    d=14
    for i in range(n):
        d=d+11
    return d


def distance_total(n):
    d=25
    dTot=25
    for i in range(2,n+1):
        d=d+11
        dTot=dTot+d
    return dTot