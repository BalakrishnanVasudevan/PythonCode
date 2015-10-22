S0 = []
S1 = []
S2 = []
y = 830
n = 1327
g = 3
q = 10
a0 = (3**10)%n
while i<n:
 i+=1
 
for p in range (1,1328):
 if p % 3 == 0:
  S0.append(p)
 elif p%3 == 1:
  S1.append(p)
 elif p%3 == 2:
  S2.append(p)

 
print ('S0:', S0)
print ('S1:', S1)
print ('S2:' ,S2)