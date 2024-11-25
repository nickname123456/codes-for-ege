def m(s):
  return s-2, s-5, s//3
ans = ['win']*20
for s in range(20, 200):
  if any(ans[x]=='win' for x in m(s)): ans +=['p1']
  elif all(ans[x]=='p1' for x in m(s)): ans +=['v1']
  elif any(ans[x]=='v1' for x in m(s)): ans +=['p2']
  elif all(ans[x]=='p1' or ans[x]=='p2' for x in m(s)): ans +=['v2']
  else: ans += ['None']
for i in range(200):
  if ans[i]=='v2':
    print(i, ans[i])
