def base(n,b):
    r=0
    T=[]
    while n>1:
        n=n//b
        T.append(n%b)
    return T