def selectionsort(source =[], *args):
 print ('original array', source)
 for i in range(len(source)-1):
  min = i
  for j in range(i+1,len(source)):
   if (source[j]<source[min]):
    min = j
  temp = source[i]
  source[i] = source[min]
  source[min] = temp
  
 print ('Sorted Array', source)




num_array = list()
num = input("Enter the number of elements in the array \n")
print ('Enter the elements of the array \n')
for i in range(int(num)):
 n = input("num:")
 num_array.append(int(n))
selectionsort(num_array)