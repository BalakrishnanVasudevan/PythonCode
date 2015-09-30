#this program takes an IP address and a subnet mask and 
#returns if the IP being requested is present in the IP address pool

import socket, struct, ipaddress
val = input("Enter the first address of the IP pool: ")
z = input("Enter the mask value: ")
n = 2**(32-int(z))
x = struct.unpack("!I", socket.inet_aton(val))[0]
y = x+n
ipval = input("Enter the IP address to be searched: ")
q = struct.unpack("!I", socket.inet_aton(ipval))[0]
flag = 0
for x in range (x,y):
 if (q == x):
  print ('IP address is present')
  x+=1
 else:
  flag+=1
  x+=1
if flag>1:
  print ('IP Address not found')

