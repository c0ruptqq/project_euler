x = pow(2, 1000)
split_list = [int(a) for a in str(x)]
print(split_list)
result = 0
for i in split_list:
    result+=i
    print(i)

print(result)