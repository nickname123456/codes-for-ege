# 7273

# 53x66y35

p = 57 # основание 

# перебор начинаем с y, тк нужно максимальное yx
for y in range(56, -1, -1):
    for x in range(56, -1, -1):
        s = 5*p**7 + 3*p**6 + x*p**5 + 6*p**4 + 6*p**3 + y*p**2 + 3*p + 5
        s1 = y*p + x
        if s%56==0:
            if int(s1**0.5) == s1**0.5: #проверка на полный квадрат (корень рациональный)
                print(x*p + y)
                input()