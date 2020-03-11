import math

de = 90
radi = de * math.pi / 180  # we mus convert degree to radiant before calculate in python
angle = [10,20,30,40,50,60,70,80,90]

def rad(x):
    c = x * math.pi / 180
    # or c = math.radians(x)
    return c

#l=float(input('l=: '))
#y=float(input('y=: ')) #x1
#A = (120*(10e-6)*y)/(l)
#A = (120*0.0000001*y)/(l)
#print(A)
#print(A*10e6) # mm to nm


#print(rad)
#print(math.degrees(rad))
print(math.sin(radi))
print(math.sin(math.radians(90)))

for i in angle:
    con = math.sin(rad(i))
    print(i,"=" ,con)
