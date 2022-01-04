
def c_triangles(p):
    s = 0
    for i in range(1,p//2+1):
        for j in range(i,p//2+1):
            h = p-i-j
            if h**2 == i**2 + j**2:
                s += 1
    return s    
b = 0
p=0
for i in range(1,1000+1):
    c = c_triangles(i)
    if b < c:
        b = c
        p = i

print(p)