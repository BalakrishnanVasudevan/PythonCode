#BalakrishnanVasudevan
#Code to find the missing number in a list of N-1 numbers

mylist = list()
sum = 0
n = int(input('Enter number of elements in the list: '))
for i in range (1,n):
 num = int(input('num: '))
 mylist.append(num)
 sum = sum+num
print ('Missing number in the list',(n*(n+1)/2)-sum)