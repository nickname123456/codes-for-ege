# №22467 КЕГЭ

from ipaddress import *
adr = ip_address('192.214.116.184') # адрес дан в условии
c=0
for mask in range(33):
    net = ip_network(f'192.214.116.184/{mask}', False) # сеть с т
    if adr==net[0] or adr==net[-1]: # если адрес который дан широковещательный и не адрес сети
        continue # применям метод скипа
    net = net[0] # это адрес сети
    net = f'{net:b}'
    if net.count('1')%5==0:
        c+=1
        print(mask)
print(c)
