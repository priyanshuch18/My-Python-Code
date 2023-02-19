def squares(a):
    cnt=0
    for i in range(1,a+1):
        j=1
        while(j*j<=i):
            if j*j==i:
                cnt=cnt+1
                j=j+1
                i=i+1
    return cnt
squares(55)

