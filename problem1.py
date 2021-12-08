"""
x = 0

for i in range(1000):
    if i%3==0 or i%5==0:
        x=x+i 

print(x)
"""

"""
def divisable(i):
    return(i%3==0 or i%5==0)

x = range(1000)
x=filter(divisable, x)
print(sum(x))
"""
x = range(1000)
x=filter(lambda i: i%3==0 or i%5==0, x)
print(sum(x))

