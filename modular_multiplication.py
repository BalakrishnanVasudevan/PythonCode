#BalakrishnanVasudevan	
#Program to generate multiplication tables and find the primitive elements
# Replace i and j with required values 
#The program prints only the primitive values, to print the table as such, replace print (i) with print (list) and remove the "if" statement

import math
list = []
for i in range (1,22):
 for j in range (1,22):
  list.append((i*j)%22)
  if ((i*j)%22)==1:
   print (i)
  j+=1
 i+=1