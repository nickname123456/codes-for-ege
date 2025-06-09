# 19716 КЕГЭ


s = open('24.21_19716.txt').read()
ans = [0]*len(s)

for i in range(1, len(s)-1):
    if s[i]!=s[i+1]:
        ans[i] = ans[i-1]+1
    else: ans[i] = 1

print(max(ans))
