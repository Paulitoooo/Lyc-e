def scientifique(n):
    assert n>0,'le nombre doit etre positif'
    c=0
    if n>=1:
        while n>10:
            n=n*0.1
            c=c+1
        print(n,'x 10^',c)
    else :
        c=-1
        while n<0.1:
            n=n*10
            c=c-1
        print(n,'x 10^',c)