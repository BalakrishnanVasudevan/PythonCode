#BalakrishnanVasudevan
##Odd and even # of elements in an array

mylist = list()
oddlist = list()
evenlist = list()

x = input("Enter the sorted elements of the first list: ") 
mylist = [int(a) for a in x.split(" ")]
count,j, i = 0,0,0
while (i<=len(mylist)) and (j<=len(mylist)):
 if (mylist[i] == mylist[j]):
  count+=1
 j+=1
 if count%2 == 0:
  evenlist.append(int(mylist[i]))
 else:
  oddlist.append(int(mylist[i]))
 i+=1
 
print ('Elements occuring an even number of times: ',evenlist)
print ('Elements occuring an odd number of times: ',oddlist)