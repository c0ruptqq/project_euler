res = 0 #TODO
def is_palindrome(n):
    s = str(n)
    return (s == s[::-1])



for i in range(100,1000):
    for g in range(100,1000):
        n = i*g
        if is_palindrome(n):
            if n > res:
                res = n
                print(res)



print(res)