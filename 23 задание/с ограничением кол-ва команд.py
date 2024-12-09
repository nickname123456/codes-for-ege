def f(st, fin, k):
  if st==fin and k==6: return 1
  if st>fin or k>6: return 0
  return f(st+1, fin, k+1)+f(st+2, fin, k+1)+f(st+3, fin, k+1)
print(f(1,20,0))
