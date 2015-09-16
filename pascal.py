import math
def pascal(rows):
 for rownum in range (rows):
  newValue=1
  PrintingList = [newValue]
  for iteration in range (rownum):
   newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
   PrintingList.append(int(newValue))
  print(PrintingList)



rows = input('Enter the number of rows \n')
pascal(rows)
print 'enter the row and column of the element to be looked up \n'
a = input('enter the row: \n')
b = input('enter the column: \n')
print 'Element \n'
print math.factorial(a)/((math.factorial(a-b))*math.factorial(b))