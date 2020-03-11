import math

a = float(input('t1=: '))
b = float(input('t2=: '))
c = float(input('t3=: '))

def hun(x):
        r =x/100
        return r

d = (hun(a)+hun(b)+hun(c))/3

#Lab 1

#print("x bar = ",d)
#print("T = ",d/10)
#print("T^2= ",(d/10)**2)

#Lab 2

print("x bar = ",d)
print("T = ",d/5)
