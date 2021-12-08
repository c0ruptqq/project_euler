

x = 0 #sum of squares
y = 0 #square of the sum

for i in range(100+1):
    x = x + i*i

y = sum(range(100+1))**2

print(x)
print(y)

print(y - x)