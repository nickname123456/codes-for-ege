f = open('файл').readlines()
s=[int(x) for x in f]
s1=[x for x in s if abs(x)%10==7 and 999<x<10000]
ma = max(s)
ans=[] #суммы элементов подходящих троек
for x, y, z in zip(s, s[1:], s[2:]):
    flag=0
    if abs(x)%10==7 and 999<x<10000:
        flag+=1
    if abs(y)%10==7 and 999<y<10000:
        flag+=1
    if abs(z)%10==7 and 999<z<10000:
        flag+=1
    if flag >= 2 and x+y+z > ma:
        ans+=[x+y+z]
print(len(ans), max(ans))



#САЛАМ ТАГИЛ РУЛИТ
