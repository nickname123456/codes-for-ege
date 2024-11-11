n= 2**12
o=0
for i in range(n):
    k=bin(i)[2:]
    if (k.count('1')+11)%5!=0:
        o+=1
print(o)