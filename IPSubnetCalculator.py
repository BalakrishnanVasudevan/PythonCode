#BalakrishnanVasudevan
#This code produces the list of IPs in a subnet when you enter the first address in the pool and the subnet mask

import socket, struct, ipaddress
val = input("Enter the first address of the IP pool: ")
z = input("Enter the mask value: ")
x = struct.unpack("!I", socket.inet_aton(val))[0]
y = x+(2**(32-int(z)))
for x in range (x,y):
 print (socket.inet_ntoa(struct.pack("!I", x)))
 x+=1
print ('Network Address: ', val)
print ('Broadcast Address: ', socket.inet_ntoa(struct.pack("!I", y)))
