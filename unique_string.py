#BalakrishnanVasudevan
#Code which does not use any data structures to determine if characters in an array are unique
#Complexity is of the order of O(n2) on account of the multiple loops


mystring = "balakrishnan"
i,j  = 0,0
for i in range(0,len(mystring)):
 count = 1
 for j in range(0,len(mystring)):
  if i != j:
   if mystring[i] == mystring[j]:
    count+=1
    j+=1
 if count == 1:
  print (mystring[i], 'is unique')
 else:
  print (mystring[i], 'occurs', count, 'times')
 i+=1 
 