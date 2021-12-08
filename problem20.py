import math

x = math.factorial(100)
print(x)
split_list = [int(a) for a in str(x)]
print(split_list)
result = sum(split_list)
print(result)