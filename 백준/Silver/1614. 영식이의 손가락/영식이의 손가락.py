p,q=map(int,open(0))
if p==1 or p==5:
    print(q*8-1+p)
else:
    if q%2:
        print(q*4-p+5)
    else:
        print(q*4+p-1)