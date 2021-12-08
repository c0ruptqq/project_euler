import math

a = 0
b = 0
c = 0

for a in range(1,1000+1):
    for b in range(a,1000-a+1):
        sq= a*a + b*b
        c = math.floor(math.sqrt(sq))
        if c*c == sq and a+b+c == 1000:
            print(a,b,c)
            print(a*b*c)
            
              