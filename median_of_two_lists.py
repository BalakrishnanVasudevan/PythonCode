#BalakrishnanVasudevan
#Merging two arrays and finding the median of the resultant array

def quicksort(arr): 
 if len(arr) <= 1:
  return arr
 else:
  return quicksort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + quicksort([x for x in arr[1:] if x>=arr[0]])

def medmer(source=[], *args):
 source = quicksort(source)
 print (source)
 n = len(source)
 if n%2==0:
  med = (source[int((n-2)/2)] + source[int(n/2)])/2
 else:
  med = source[int(n/2)]
 return med  
 


list1 = list()
list2 = list()
x = input("Enter the sorted elements of the first list: ") 
list1 = [int(a) for a in x.split(" ")]
y = input("Enter the sorted elements of the second list: ")
list2 = [int(b) for b in y.split(" ")]
merged = list1 + list2
print (merged)
print (medmer(merged))
