def gcd(num1,num2):
    if num1<num2:
        a,b = num1,num2
    else:
        a,b = num2,num1
    t = a
    while a>=1:
        if(b%a==0)&(t%a==0):
            return a
        a-=1

nu1 = input('Enter 2 numbers')
nu2 = input()
n1 = int(nu1)
n2 = int(nu2)
x = gcd(n1,n2)
print ('gcd of ' +str(n1)+' '+str(n2)+' is '+str(x) )
