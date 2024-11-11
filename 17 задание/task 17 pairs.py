f = open('17-410.txt').readlines()

s = [int(x) for x in f]
m = min(s)
ans = [] # суммы элементов подходящих
for x, y in zip(s, s[1:]):
    if x%16 == m or y%16==m:
        ans += [x+y]

print(len(ans), max(ans))
