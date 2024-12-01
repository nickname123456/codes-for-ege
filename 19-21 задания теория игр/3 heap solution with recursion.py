from functools import *
def m(s):
    a, b, c = s
    return (a+3, b, c), (a, b+3, c), (a, b, c+3), (a+13, b, c), (a, b+13, c), (a, b, c+13), (a+23, b, c), (a, b+23, c), (a, b, c+23)
@lru_cache(None)
def g(s):
    a, b, c = s
    if a+b+c>72: return 'win'
    '''if s>60: return 'p1'''
    if any(g(x)=='win' for x in m(s)): return 'p1'
    if any(g(x)=='p1' for x in m(s)): return 'v1'
    if any(g(x)=='v1' for x in m(s)): return 'p2'
    if all(g(x)=='p1' or g(x)=='p2' for x in m(s)): return 'v2'
a=2
for b in range(23, 0, -1):
    s=(a, b, 2*b)
    if g(s)=='v1':
        print(g(s), s)
