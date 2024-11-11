from itertools import *

n = 0

for s in product('БЕНРСТЬЯ', repeat=5):
    s1=''.join(s)
    n+=1
    if s1[0]=='Р' and s1.count('Ь')==0 and n%2==0:
        print(n)