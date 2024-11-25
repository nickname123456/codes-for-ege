from functools import *
def m(s):
  return s//3, s-5, s-2
@lru_cache(None)
def g(s):
  if s<20: return 'win'
  if any(g(x)=='win' for x in m(s)): return 'p1'
  if all(g(x)=='p1' for x in m(s)): return 'v1'
  if any(g(x)=='v1' for x in m(s)): return 'p2'
  if all(g(x)=='p1' or g(x)=='p2' for x in m(s)): return 'v2'
for i in range(20, 200):
  if g(i)=='v2':
    print(i, g(i))
