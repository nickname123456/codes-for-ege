from itertools import permutations
s=0
for i in permutations('ДЕЙКСТРА', r=6):
    x=''.join(i)
    if any(sub in x for sub in ['ЙД','ЙК','ЙС','ЙТ','ЙР']):
        s+=1
print(s)