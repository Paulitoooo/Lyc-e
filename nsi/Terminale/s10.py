from random import randint
L1 = [randint(0,100) for i in range(50)]
L1.sort()
L2 = [randint(0,100) for i in range(50)]
L2.sort()

def fusion(L1,L2):
    L=[]
    i1=0
    i2=0
    while i1<len(L1) and i2<len(L2):
        if L1[i1]<L2[i2]:
            L.append(L1[i1])
            i1=i1+1
        else:
            L.append(L2[i2])
            i2=i2+1
    if i1< len(L1)-1:
        L = L + L1[i1:]
    if i2 < len(L2)-1:
        L = L + L2[i2:]
