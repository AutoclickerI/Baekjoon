k,x,y=map(int,open(0))
d=y//x
if (k-1)*d>=y%x:
    print(y)
else:
    print((d+1)*x)