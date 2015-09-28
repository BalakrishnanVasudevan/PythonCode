def bubblesort(source =[], *args):
 print ('original array', source)
 for k in range(1,len(source)-1):
  for i in range(0,len(source)-k):
   if (source[i]>source[i+1]):
    temp = source[i]
    source[i] = source[i+1]
    source[i+1] = temp
   
  
 print ('Sorted Array', source)




num_array = list()
num = input("Enter the number of elements in the array \n")
print ('Enter the elements of the array \n')
for i in range(int(num)):
 n = input("num:")
 num_array.append(int(n))
bubblesort(num_array)   