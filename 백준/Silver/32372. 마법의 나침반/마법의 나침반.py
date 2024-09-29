N,M=map(int,input().split())
x=y=1
X=Y=N
for _ in[0]*M:
    a,b,d=map(int,input().split())
    if d==1:
        X=min(X,a-1)
        y=Y=b
    if d==2:
        X=min(X,a-1)
        y=max(y,b+1)
    if d==3:
        x=X=a
        y=max(y,b+1)
    if d==4:
        x=max(x,a+1)
        y=max(y,b+1)
    if d==5:
        x=max(x,a+1)
        y=Y=b
    if d==6:
        x=max(x,a+1)
        Y=min(Y,b-1)
    if d==7:
        x=X=a
        Y=min(Y,b-1)
    if d==8:
        X=min(X,a-1)
        Y=min(Y,b-1)

print(x,y)