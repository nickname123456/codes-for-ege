# 6674

s=open('24-263.txt').read()

left=right=0
ans=[]

while right < len(s):
    s1 = s[left:right]
    if s1.count('Z')>=120:
        ans+=[right-left]
        left+=1
    else:
        right+=1

print(min(ans))
