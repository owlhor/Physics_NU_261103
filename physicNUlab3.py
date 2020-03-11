# PhysicNUlab3
import math
#mode = 1
mode = 2

if mode == 1:  # Lambda
        lis=[6,5,4,3,2]
        l = float(input('Ropelength= '))
        for i in lis:
                A = (2*l)/i
                #print(i , A, A**2)
                print("{:d} {:.4f} {:.4f}".format(i , A, A**2))

if mode == 2: # m,F ,V
        u = 0.001159
        #lis=[34.30,47.45,77.95,139.00,330.40] # weight1
        lis=[26.05,38.80,62.80,122.80,271.20] # weight2
        #ran=[6,5,4,3,2]
        for i in lis:
                
                print("F ={:.3f}".format((i/1000)*9.80))
        print(" ")
        for f in lis:
                
                print("V ={:.3f}".format(math.sqrt((f/1000)/u)))





