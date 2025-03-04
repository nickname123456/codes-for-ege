def sum_len(x, y, f): # возвращает сумму всех длин от точки (x, y) до всех остальных точек в списке f
    lens = []
    for xi, yi in f:
        lens += [((xi-x)**2 + (yi-y)**2)**0.5]
    return sum(lens)


f = open('kl1.txt').readlines()
for i in range(len(f)): # Перебираем все точки и делаем их координаты float
    f[i] = [float(x) for x in f[i].split()]

ans = []
for x, y in f: # Перебираем все точки
    ans += [sum_len(x, y, f)] # И записываем их суммы длин

n = ans.index(min(ans)) # Какой индекс у точки, с минимальной суммой длин?
print(f[n]) # Центр кластера - точка, с минимальным расстоянием до всех других точек