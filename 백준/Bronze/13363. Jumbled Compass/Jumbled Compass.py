p,q=map(int,open(0))
a=(p-q)%360
b=(q-p)%360
if a<b:
    print(-a)
else:
    print(b)