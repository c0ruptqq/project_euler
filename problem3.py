def is_prime(n):
    if n%2==0:
        return False
    else:
        for i in range(3,n//2,2):
            if n%i==0:
                return False
        return True
n = 600851475143
d = 3
l = 0
while d <= n:
    if n%d==0 and is_prime(d):
        print(d)
        n = n//d
        l = d
    else:
        d = d + 2 

print(l)