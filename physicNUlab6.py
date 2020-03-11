import math

m1 = 30 #float(input('m1=: '))
m2 = float(input('m2=: '))
m3 = float(input('m3=: '))
m4 = 79.63 #float(input('m4=: '))

pst = 0.9971

#s = ((m3-m1)/(m2-m1))*pst

p =((m2-m1)/((m4-m1)-(m3-m2)))*pst

print("P = ",p)
