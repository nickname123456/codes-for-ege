alf='0123456789ab'
def per12(x):
    alf='0123456789ab'
    k=''
    while x>0:
        d=x%12
        k=alf[d]+k
        x//=12
    return k
s=''
for N in range(1,1000):
    n=per12(N)
    if int(n,12)%4==0:
        n='2'+n+'64'
    else:
        for i in n:
            if alf.find(i)>=alf.find(s):
                s=i
        n=n+s
    r=int(n,12)
    if r>1799 and r<2000:
        print(r)