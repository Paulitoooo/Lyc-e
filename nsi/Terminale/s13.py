L=[(8,480),(5,400),(4,300),(1,50)]
Ma=[(6,480),(5,350),(4,300),(1,50)]
Me=[(9,810),(6,720),(5,550),(4,400),(1,80)]
J=[(7,910),(6,720),(4,480),(3,270),(2,260),(1,200)]

def glouton(j):
    T=j.copy()
    T.sort(key=lambda L:L[1], reverse=True)
    m=10
    p=0
    v=[]
    for i in T:
        if i[0]<=m:
            p=p+i[1]
            m=m-i[0]
    return p

def codeBin(n,nb):
    T=[0 for i in range(nb)]
    c=-1
    for i in range(nb):
        d=n%2
        n=n//2
        T[c]=d
        c=c-1

    return T

def brutus(n):
    return [codeBin(i,n) for i in range(2**n)]

def forceBrute(L):
    L2 = brutus(len(L))
    for i in L2:
        p=0
        m=0
        for j in range(len(i)):
            if i[j]==1:
                m=m+L[j][0]
                p=p+L[j][1]
        i.append(m)
        i.append(p)
    return L2

def sac(L,p):
    if len(L)==0:
        return 0
    if L[-1][0]>p:
        return sac(L[:-1],m)
    return max(sac(L[:-1],m) , L[-1][1] + sac(L[:-1],m-L[-1][0]))
