import math
inc = 3
d = 0 
n = 3

def factors(z):
    f = 2
    total = 2
    while f <= z:
        if z%f ==0:
            z = z//f
            total +=1
        else:
            f +=1

    return(total)            
print(factors(28))
"""
while d < 500:
    n += inc
    d = factors(n)
    inc += 1
    print(n,d)
"""

"No solution yet"
print(n)