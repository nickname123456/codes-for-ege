def sum_len(x, y, f):
    lens = []
    for xi, yi in f:
        lens += [((x-xi)**2 + (y-yi)**2)**0.5]

    return sum(lens)


f = open('3kl.txt').readlines()
for i in range(len(f)):
    f[i] = [float(x) for x in f[i].split()]

min_len = 999999
min_i = 0

max_len = 0
max_i = 0

for i in range(len(f)):
    x = f[i][0]
    y = f[i][1]
    lens = sum_len(x, y, f)
    if lens<min_len:
        min_len=lens
        min_i=i

    if lens>max_len:
        max_len=lens
        max_i = i

print(f'корды центра 3 кластер: {f[min_i]}')
print(f'корды antiцентра 3 кластер: {f[max_i]}')
