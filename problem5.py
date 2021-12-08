res = None
n = 1

def is_divisable(n):
    k = True
    for i in range(20,1, -1):
        if not n%i==0:
            k = False
            break
    return k



while True:
    c=3*5*7*11*13*17*19*n
    if is_divisable(c) and (res is None or c < res):
        res = c
        break
    n+=1

print(res)
