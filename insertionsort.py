def insertionsort(source =[], *args):
 print ('original array', source)
 for i in range(len(source)-1):
  value = source[i]
  hole = i
  while (hole>0 && source[hole-1]>value):
   source[hole]=source[hole-1]
   hole-=1
  source[hole]=value
  
 print ('Sorted Array', source)




num_array = list()
num = input("Enter the number of elements in the array \n")
print ('Enter the elements of the array \n')
for i in range(int(num)):
 n = input("num:")
 num_array.append(int(n))
insertionsort(num_array)