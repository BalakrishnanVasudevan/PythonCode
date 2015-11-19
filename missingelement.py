#BalakrishnanVasudevan
#Code to find the missing number in a list of N-1 numbers

mylist = list()
sum = 0
n = int(input('Enter number of elements in the list: '))
for i in range (1,n):
 num = int(input('num: '))
 mylist.append(num)
b = num[0]
for j in range (1,len(mylist)):
 b = b^mylist[j]
for k in range 
