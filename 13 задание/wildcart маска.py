from ipaddress import *

wild = '0.0.7.255'.split('.') # разбиваем вилд по байтам
mask = [0]*4 # ппустая маска
for i in range(4):
    s = bin(int(wild[i]))[2:].zfill(8) #переводим все байты в двоичную запись
    s = s.replace('0', '*').replace('1', '0').replace('*', '1') # реверсим цифры для маски
    s = int(s, 2)
    mask[i] = str(s) 
mask = '.'.join(mask) # готовая маска

c=0
net = ip_network(f'172.16.80.0/{mask}', 0)
for i in net:
    i = f'{i:b}'
    if i.count('1')%3!=0: c+=1
print(c)
