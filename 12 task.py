n= 68 *'9'
while '22222' in n or '9999' in n:
    if '22222' in n:
        n=n.replace('22222','99',1)
    else:
        n=n.replace('9999','29',1)
print(n.count('9'))
print(n)