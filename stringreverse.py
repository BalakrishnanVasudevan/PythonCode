#BalakrishnanVasudevan
#Code to reverse a string without using Extended Slices
#When using Extended Slices: '<string>'[::-1]


def reverse(mystring):
 if len(mystring) == 1:
  return mystring
 else:
  return reverse(mystring[1:])+mystring[0]

mystring = input('Enter the string: ')
print (reverse(mystring))