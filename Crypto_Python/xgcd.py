def xgcd(a,b):
 if b == 0:
  return [1,0,a]
 else:
  x,y,d = xgcd(b, a%b)
  return [y, x - (a//b)*y, d] # Note that a//b is floor(a/b) in Python