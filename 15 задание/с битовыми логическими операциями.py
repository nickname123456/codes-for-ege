# 7262

def f(a):
    for x in range(0, 99999):
        if ( ((x&32765 !=0) or (x&22635 != 0)) <= (x&a>0) ) == 0:
            return False
    else:
        return True

for a in range(1, 9999999):
    if f(a):
        print(a)
        input()