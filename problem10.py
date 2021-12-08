lp = [2,3,5,7,11]

p = 13
import math

def is_prime(n):
    sq = math.floor(math.sqrt(n))
    i = 0
    while i <= sq:
        if n%lp[i] == 0:
            return False
        else:
            i +=1
    return True

     

while True:
    if is_prime(p):
        if p < 2000000:
            lp.append(p)
            print(p)
        else: break
    p+=2

print(sum(lp))

