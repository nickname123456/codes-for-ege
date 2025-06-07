# 4964 КЕГЭ

alf = '0123456789abcdefghijk'
def f(x):
    for y in alf:
        a = int(f'12{y}{x}9', 21)
        b = int(f'36{y}99', 21)
        if (a+b) % 18 != 0: # если хоть 1 у не подходит
            return False # ливаем
    return True

for x in alf:
    if f(x):
        y = 5
        a = int(f'12{y}{x}9', 21)
        b = int(f'36{y}99', 21)
        print((a+b)//18)
        input()    
