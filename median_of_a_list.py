#BalakrishnanVasudevan
#Code to find median in a sorted list

def median(source=[], *args):
 n = len(source)
 if n%2==0:
  med = (source[int((n-2)/2)] + source[int(n/2)])/2
 else:
  med = source[int(n/2)]
 return med  

nlist = list()
n = input('Enter the number of elements in the list \n')
print ("Enter the elements: \n")
for i in range(int(n)):
 x = input('n:')
 nlist.append(int(x))
print (median(nlist))
# print ("Insert new element \n")
# z = input('n: ')
# nlist.append(int(z))
# print(median(nlist))



  
