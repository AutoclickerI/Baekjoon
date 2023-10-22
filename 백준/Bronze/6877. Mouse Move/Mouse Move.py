c,r=map(int,input().split())
x=y=0
while 1:
    p,q=map(int,input().split())
    X,Y=max(0,min(x+p,c)),max(0,min(y+q,r))
    if(p,q)==(0,0):
        break
    x,y=X,Y
    print(X,Y)