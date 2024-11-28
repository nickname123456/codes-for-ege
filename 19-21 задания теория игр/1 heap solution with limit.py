# 4384 - ограничение в кол-ве камнях
from functools import *

# главное различие от других задач - не всегда можно сделать все ходы
def m(s):
  hods = [s+1]
  if s*2<=80:
    hods+=[s*2]
  return hods

# универсальная часть
@lru_cache(None)
def g(s):
  hods = m(s)
  if s>=61: return 'win'
  if any(g(x)=='win' for x in hods): return 'p1'
  if all(g(x)=='p1' for x in hods): return 'v1'
  if any(g(x)=='v1' for x in hods): return 'p2'
  if all(g(x)=='p1' or g(x)=='p2' for x in hods): return 'v2'



# эта часть зависит от вопросов
c=0
p2=[]
v2=[]
for i in range(1, 61):
  if g(i)=='p1':
    c+=1

  if g(i)=='p2':
    p2+=[i]

  if g(i)=='v2':
    v2+=[i]

print('19', c)
print('20', p2[:2])
print('21', v2)