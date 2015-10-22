from random import randint
from fractions import gcd

n = int(input('Enter the number to be factorized \n'))
i,xi,k = 1, randint(0,n-1), 2
y = xi
while i<n:
 i+=1
 xi=((xi**2)-1)%n
 d=gcd(y-xi,n)
 if d!=1 and d!=n:
  print (d)
 if i==k:
  y=xi
  k=2*k