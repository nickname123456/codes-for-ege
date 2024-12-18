n= 4**644+4**322+16**35-64**3

def f4(x):
    s=''
    while x>0:
        d=x%4
        s=str(d)+s
        x//=4
    return s
print(f4(n))
print(f4(n).count('3'))
