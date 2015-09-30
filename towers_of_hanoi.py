#BalakrishnanVasudevan
#Python implementation of the Towers of Hanoi

def hanoi(n, source, mid, dest):
 if n>0:
  #pop n-1 elements to the intermediate pole
  hanoi(n-1,source,dest,mid)
  #pop the last element in the source pole to the destination
  if source:
   dest.append(source.pop())
  #pop the elements in the intermediate pole to the destination
  hanoi(n-1,mid,source,dest)
  
  



source = [i for i in range (1,64)]
print (source)
mid = []
dest =[]
hanoi(len(source), source, mid, dest)

print (source, mid, dest)