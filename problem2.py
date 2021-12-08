a = 1
b = 2
x=0
l = []
print(a)


while b < 4000000:
    if b%2==0:
        l.append(b)
        x=x+b
    print(b)
    next = a+b
    a=b
    b=next

print("Result through X:")    
print(x)
print("Result through a list:")
print(sum(l))  
