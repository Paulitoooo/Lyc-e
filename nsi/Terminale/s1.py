#Exo 1

montab1= ['5', '10', '8', '1', '100']
print(sorted(montab1))


montab1 = ['a', 'b', 'c', 'd']
montab2 = montab1
montab2[1]='e'
print(montab1)
print(montab2)

#Exo 2

TAB5= [i for i in range(0,101,5)]
TAB53= [i for i in TAB5 if i%3==0]

from random import *

TAB10= [[randint(0,10),randint(0,10)] for i in range(10)]