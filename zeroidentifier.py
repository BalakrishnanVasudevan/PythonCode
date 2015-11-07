#BalakrishnanVasudevan
#Code to identify zeros in a list and replace them


mylist = list()
mynewlist = list()
count = 0
n = input('Enter the number of elements in the list: ')
for i in range (int(n)):
 num = int(input('num: '))
 if num != 0:
  mynewlist.append(num)
 else:
  count+=1
for k in range (0,count):
 mynewlist.append(0)
print (mynewlist)
