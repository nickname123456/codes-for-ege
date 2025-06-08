# 4040 КПоляков

ans = set()

def f(st, k):
    k+=1
    ans.add(st)
    if k>12: return 

    f(st+1, k)
    f(st*2-3, k)

f(3, 0)
print(len(ans))
