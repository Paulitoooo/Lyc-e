#Exo 1

tup=('A', 'C', 'Y', 'E', 'Z', 'F')
tup=tup[:4]+tup[-1:]
tup=tup[:2]+('D',)+tup[-2:]
tup=tup[:1]+('B',)+tup[-4:]
print(tup)

#Exo 2
from random import *

def creerTuple():
    classe=()
    for i in range(35):
        classe=classe+(randint(1,365),)
    return classe

def testDouble(tu):
    for i in tu:
        if tu.count(i)>1:
            return True
    return False


c = 0
for i in range(10000):
    if testDouble(creerTuple()):
        c = c + 1
print(c)