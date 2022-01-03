s = 1

#one million is less than 2^20 so the first half of the binary
#palindrom would be less than 2^11-1 
for i in range(1, 2047+1):
    b = "{0:b}".format(i)
    rb = b[::-1]
    #print(b)
    #print(rb)
    for v in [b+rb, b+"0"+rb, b+"1"+rb]:
        d = int(v, 2)
        #print(d)
        if d < 1000000 and str(d) == str(d)[::-1]:
            print(v)
            print(d)
            s+= d

print(s)


