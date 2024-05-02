[c,r],*l,_=[map(int,i.split())for i in open(0)]
x=y=0
for p,q in l:
    X,Y=max(0,min(x+p,c)),max(0,min(y+q,r))
    x,y=X,Y
    print(X,Y)