lp = [2,3,5,7,11,13]

p = 13


def is_prime(n):
    for p in lp:
        if n%p == 0:
            return False
    return True

while len(lp) < 10002:
    if is_prime(p):
        lp.append(p)
        print(p)
    else:
        p+=2

print(lp[10000])

