#BalakrishnanVasudevan
#Exhaustive search algorithm for DLP

p,y,g = 1327,582,3
for i in range (1,p-1):
 if y == ((g**i)%p):
  print ('x: ', i)