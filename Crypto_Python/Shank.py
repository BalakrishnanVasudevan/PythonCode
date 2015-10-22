#BalakrishnanVasudevan
#Shank's Giant Step - Baby Step algorithm

import math

giant = []
baby = []
y,g,p,z = 940,3,1327,0
m = math.ceil(math.sqrt(p))
number = [i for i in range (0,m+1)]
for i in range (0,m+1):
 giant.append((3**(m*i)%p))
for j in range (0,m+1):
 baby.append((y*(g**j)%p))
for x in range (0,m):
 for y in range (0,m):
  if giant[x]==baby[y]:
   z = ((x*m)-y)%(p-1)
  y+=1
 x+=1


print ('i:', number)
print ('Giant:', giant)
print ('j:', number)
print ('Baby:', baby)
print ('z:',z)
   
  
  