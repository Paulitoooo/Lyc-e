from random import randint

def Premier(N):
    rep=True
    for i in range(2,N):
        if N%i==0:
            rep=False
    return rep

def aleaprem():
    test=False
    while test==False:
        A=randint(2,997)
        test=Premier(A)

    return A