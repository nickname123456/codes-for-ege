# 7194

s=open('24-280.txt').read()
left=right=0
ans=[]

while right <len(s):
    s1=s[left:right]
    while any(s1.count(i)>5 for i in 'XYZ'):
        left+=1
        s1=s[left:right]
    if all(s1.count(i)==5 for i in 'XYZ'):
        ans+=[right-left]
    right+=1    

print(max(ans))