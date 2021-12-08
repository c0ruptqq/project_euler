memo={}

def collatz(z, steps):
    if z==1:
        return(steps)
    else:
        if z in memo:
            return(memo[z])
        else:        
            if z%2 == 0:
                s=collatz(z//2,steps+1)
            else:
                s=collatz(z*3 + 1,steps+1)
            s=s+1
            memo[z]=s
            return(s)
        


chain = 0
best_chain = 0
best_start = 0
for i in range(2, 1000000):
    chain = collatz(i,0)
    
    
    if chain > best_chain:
        best_chain = chain
        best_start = i


print(best_start)