# 7560

def f(a):
    for x in range(1, 999):
        for y in range(1, 999):
            if (  (x+y<=30) or (y<=x+2) or (y>=a) ) == 0:
                return False
    else:
        return True

ans = []
for a in range(0, 999999):
    if f(a):
        print(a)
        ans+=[a]
print(f'Ответ: {max(ans)}')