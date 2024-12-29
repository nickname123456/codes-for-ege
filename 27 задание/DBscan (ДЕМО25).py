from math import dist

clustersA = []
clustersB = []

data = []

for line in open('27_A_17882.txt'):
    x,y = [float(x) for x in line.split()]
    data.append([x, y])

while data:
    clustersA.append([data.pop()])
    for p1 in clustersA[-1]:
        neighbours = [p for p in data if dist(p1, p) < 1]
        clustersA[-1] += neighbours
        for p in neighbours:
            data.remove(p)

data = []

for line in open('27_B_17882.txt'):
    x,y = [float(x) for x in line.split()]
    data.append([x, y])

while data:
    clustersB.append([data.pop()])
    for p1 in clustersB[-1]:
        neighbours = [p for p in data if dist(p1, p) < 1]
        clustersB[-1] += neighbours
        for p in neighbours:
            data.remove(p)

def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxA = sum(x for x, y in centersA) / 2 * 10000
pyA = sum(y for x, y in centersA) / 2 * 10000
pxB = sum(x for x, y in centersB) / 3 * 10000
pyB = sum(y for x, y in centersB) / 3 * 10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))