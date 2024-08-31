x=y=10
X=Y=-10
for i in[*open(0)][1:]:
    a,b,c,d=map(int,i.split())
    x=min(x,a)
    y=min(y,b)
    X=max(c,X)
    Y=max(d,Y)
    print(Y-y+X-x<<1)