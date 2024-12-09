def f(st, fin):
  if st==fin: return 1
  if st>fin: return 0
  if st==13: return 0
  return f(st+2, fin)+f(st*3, fin)+f(st**2, fin)
print(f(3,49))
