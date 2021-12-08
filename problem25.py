f1 = 1
f2 = 1
term = 2
result = 0
while len(str(result)) <= 999:
    term += 1
    result = f1 + f2
    f2 = f1
    f1 = result
    print(f1)
    print(term)

print(result)
print(len(str(result)))
print(term)