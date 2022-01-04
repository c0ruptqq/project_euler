
def same_digits(a,b):
    return (sorted(str(a)) == sorted(str(b)))


x = 1
while True:
    failed=False
    for i in range (2,6+1):
        if not same_digits(x, x*i):
            failed=True
            break
    if failed:
        x +=1
    else:
        print(x)
        break
