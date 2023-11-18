t,n,a,b,c=map(int,open(0).read().split())
if t-1:
    print(min(a,b,c))
else:
    print(max(max(a+b-n,0)+c-n,0))
    