#Sujet M:

def rendu(r):
    L = (50,20,10,5,2,1)
    D = {}
    c = 0
    if r == 0:
        return D
    while r != 0:
        if r-L[c]>=0:
            r=r-L[c]
            if L[c] in D:
                D[L[c]]=D[L[c]]+1
            else:
                D[L[c]]=1
        else:
            c=c+1
    return D