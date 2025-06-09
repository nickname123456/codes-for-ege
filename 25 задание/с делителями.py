# 21909 КЕГЭ
def R(n):
    de = set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            de.add(i)
            de.add(n//i)
    return sum(de)
c = 0
for x in range(500_000, 10**10):
    r = R(x)
    if str(r)[-1]=='6':
        c+=1
        print(x, r)
    if c==5:
        break
