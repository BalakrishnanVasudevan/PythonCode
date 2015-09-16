rows = 5
for rownum in range (rows):
    newValue=1
    print 'rownum=', rownum
    PrintingList = [newValue]
    for iteration in range (rownum):
    	print 'iteration', iteration
        newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
        PrintingList.append(int(newValue))
        print 'newValue=', newValue
    print(PrintingList)
