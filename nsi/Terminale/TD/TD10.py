#TD10:
#Exo 4.1:

def moyenne(tab):
    assert tab==[],"Le tableau doit être non-vide"
    n=len(tab)
    t=0
    for i in tab:
        t=t+i
    return t/n



#Exo 6.1 :
def rendu(n):
    n1=0
    n2=0
    n3=0
    while n>0:
        if n>=5:
            n1=n1+1
            n=n-5
        elif 5>n>=2:
            n2=n2+1
            n=n-2
        else:
            n3=n3+1
            n=n-1
    print([n1,n2,n3])