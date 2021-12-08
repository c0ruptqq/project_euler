size = 21
grid = [[0]*size]*size
grid[size-1][size-1] = 0
for i in range(0,size-1):
    grid[size-1][i] = 1
    grid[i][size-1] = 1
    
for r in range(size-2,-1,-1):
    for c in range(size-2,-1,-1):
        print(r,c)
        grid[r][c] = grid[r+1][c] + grid[r][c+1]

result = grid[0][0]
print(result)