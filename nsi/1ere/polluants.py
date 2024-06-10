def pol(rejets,n):
    while rejets>2000:
        rejets=rejets-(rejets*0.08)
        n=n+1
    print(n)