'''
УСЛОВИЕ:
Определите минимальную длину подстроки, 
в которой ровно три тройки BAD или FAT.


Например, в строке SDFATFDBADZZSFATBADGHTBAD 
есть три подходящие подстроки 
FATFDBADZZSFAT, 
BADZZSFATBAD и 
FATBADGHTBAD. 

Минимальная длина 12.
'''




s = open('24_9169.txt').read()
l=r=0
ans = []

while r<len(s):
    s1 = s[l:r]
    while s1.count('BAD') + s1.count('FAT')>3: # если троек больше нужного
        l+=1 # двигаем левый край
        s1 = s[l:r]

    while s1.count('BAD') + s1.count('FAT')==3: # если троек нужное колво то можем подвигать еще в лево, чтобы получить минимум
        if (s[l]+s[l+1]+s[l+2]) == 'BAD' or (s[l]+s[l+1]+s[l+2]) == 'FAT': # если левый край дошел до тройки,
            break # то не трогаем и бросаем двигать левый край
        l+=1
        s1 = s[l:r]

    if s1.count('BAD') + s1.count('FAT')==3: # если по условию все норм, то добавляем в ответ
        ans += [len(s1)]

    r+=1
print(min(ans))
