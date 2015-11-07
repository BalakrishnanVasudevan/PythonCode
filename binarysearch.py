#BalakrishnanVasudevan
#Binary Search Algorithm

def binsearch(mylist, y):
 if len(mylist) == 0:
  return False
 else: 
  n = len(mylist)//2
  if y == mylist[n]:
   return True
  else:
   if y<mylist[n]:
    return binsearch(mylist[:n],y)
   if y>mylist[n]:
    return binsearch(mylist[n+1:],y)

mylist = list()
x = input("Enter the sorted elements of the list: ") 
mylist = [int(a) for a in x.split(" ")]
y = int(input("Enter the element to be searched for: "))
print (binsearch(mylist,y))