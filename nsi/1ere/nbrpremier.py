def premier(N):
    rep=True
    for i in range(2,N):
        if N%i==0:
            rep=False
    return rep
