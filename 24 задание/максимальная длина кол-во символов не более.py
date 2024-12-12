# 6675

s=open('24-263.txt').read()
left=right=0
ans=[]
while right <len(s):
    s1=s[left:right]
    if s1.count('Y')>150:
        ans+=[right-left-1]
        left+=1
    else:
        right+=1
        
print(max(ans))        