#BalakrishnanVasudevan
#Array Re-ordering

mylist = list()
indexlist = list()
mynewlist = list()
n = int(input('Enter number of elements: '))
for i in range(0,n):
 num = int(input('num: '))
 mylist.append(num)
print ('Enter index array \n')
for j in range (0,n):
 xum = int(input('n: '))
 indexlist.append(xum)
for x in range (0,n):
 mynewlist.append(mylist[indexlist[x]])
print (mynewlist)