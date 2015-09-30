#BalakrishnanVasudevan
#Tricky question from a Google Interview

array = [False for x in range (0,101)]
for skip in range (1,100):
 for i in range (0,100):
  array[i]= not(array[i])
  i+=skip
 skip+=1
print (array[9])
