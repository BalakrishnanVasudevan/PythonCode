#BalakrishnanVasudevan
#Code to check if there are unique characters in the string


mystring = "balakrishnan"
alpha = [0 for i in range (0,26)]
print (alpha)
for j in range (0,len(mystring)):
 alpha[ord(mystring[j])-97]+=1
 j+=1
print (alpha)
for i in range (0,26):
 if alpha[i]==1:
  print (chr(97+i),'is unique')
 if alpha[i]>1:
  print (chr(97+i),'occurs',alpha[i],'times')
 i+=1