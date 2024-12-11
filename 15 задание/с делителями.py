# 7559

def de(n, m):
    return n%m==0

def f(a):
    for x in range(1, 9999):
        if (de(x, 33) <= ((not de(x, a)) <= (not de(x, 242)))) == 0:
            return False
    else:
        return True

ans = []
for a in range(1, 999):
    if f(a):
        print(a)
        ans+=[a]
print(f'Ответ: {max(ans)}')
