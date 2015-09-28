def quicksort(arr): 
 if len(arr) <= 1:
  return arr
 else:
  return quicksort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + quicksort([x for x in arr[1:] if x>=arr[0]])

num_array = list()
num = input("Enter the number of elements in the array \n")
print ('Enter the elements of the array \n')
for i in range(int(num)):
 n = input("num:")
 num_array.append(int(n))
print (quicksort(num_array))