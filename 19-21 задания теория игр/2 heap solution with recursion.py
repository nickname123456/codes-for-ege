from functools import *
def m(s):
  a, b = s
  return (a*3, b), (a, b*3), (a+1, b), (a, b+1)
@lru_cache(None)
def g(s):
  a, b = s
  if a+b>45: return 'win'
  if any(g(x)=='win' for x in m(s)): return 'p1'
  if all(g(x)=='p1' for x in m(s)): return 'v1'
  if any(g(x)=='v1' for x in m(s)): return 'p2'
  if all(g(x)=='p1' or g(x)=='p2' for x in m(s)): return 'v2'
a=4
for b in range(44, 1, -1):
  s=(a,b)
  if g(s)=='v1': print(s, g(s))
