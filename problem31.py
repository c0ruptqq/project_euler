#count = 0
#coins = [0,0,0,0,0,0,0,1]
#den =   [1,2,5,10,20,50,100,200]
#
#def split(coins,den):
#    #find smallest coin#
#    i = 1
#    while not (coins[i]>0):
#        i += 1
#    # remove 1 smallest coin
#    coins[i] -= 1
#    cost = den[i]
#    #change into smaller coins
#    while cost > 0:
#        i -= 1
#        coins[i] += cost // den[i]
#        cost = cost%den[i]
#
#while not(sum(coins[1:]) == 0):
#    print(coins)
#    split(coins,den)
#    count += 1
#
#
#print(count)

rem = 200
count = 0
for a in range(rem, 0-1, -200):
    for b in range(a, 0-1, -100):
        for c in range(b, 0-1, -50):
            for d in range(c, 0-1, -20):
                for e in range(d, 0-1, -10):
                    for f in range(e, 0-1, -5):
                        for g in range(f, 0-1, -2):
                            print(a,b,c,d,e,f,g)
                            count += 1
                        
    

print(count)