def mergesort(source =[], *args):
 n = len(source)
 if(n<2):
  return source
 else:
  mid = int(n/2) 
  l = source[:mid]
  r = source[mid:]
  l1 = mergesort(l)
  r1 = mergesort(r)
 a = list()
 nl = len(l1)
 nr = len(r1)
 i,j = 0,0
 while (i<nl) and (j<nr):
  if (l1[i]>r1[j]):
   a.append(r1[j])
   j+=1
  else:
   a.append(l1[i])
   i+=1
 a += l1[i:]
 a += r1[j:]
 return a
  
  




num_array = list()
num = input("Enter the number of elements in the array \n")
print ('Enter the elements of the array \n')
for i in range(int(num)):
 n = input("num:")
 num_array.append(int(n))
print (mergesort(num_array))