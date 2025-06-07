# 6271 КПоляков

f = open('17-367.txt').readlines()
s = [int(i) for i in f]

lens = [0]*len(s) # список с комбо
for i in range(1, len(s)-1): # берем со ВТОРОГО до ПРЕДпоследнего
    x = s[i-1]
    y = s[i]
    z = s[i+1]
    if y%x==0 or y%z==0: # если нас устраивает
        lens[i] = lens[i-1]+1 # то в комбо +1
    else:
        lens[i]=0 # Иначе комбо обнуляется

len_max = max(lens) # макс длина комбо
i_max = lens.index(len_max) # где комбо заканчивается

otvet = 0
for i in range(i_max, i_max-len_max, -1): # перебираем все числа в этом комбо
    otvet+=s[i]

print(len_max, otvet)