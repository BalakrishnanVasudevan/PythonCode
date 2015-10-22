def isPrime(a):
 return not ( a < 2 or any(a % i == 0 for i in range(2, int(a ** 0.5) + 1)))

def phi(n = 22):
 y = n
 for i in range(2,n+1):
  if isPrime(i) and n % i == 0:
   y *= 1 - 1.0/i
 print(y)