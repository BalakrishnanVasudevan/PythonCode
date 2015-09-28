def reverse(source=[], *args):
 n = len(source)
 rlist = list()
 i = 0
 while i < n:
  rlist.append(source[n-i-1])
  i+=1
 return rlist




num_array = list()
num = input("Enter the number of elements in the array \n")
print ('Enter the elements of the array \n')
for i in range(int(num)):
 n = input("num:")
 num_array.append(int(n))
print (reverse(num_array))