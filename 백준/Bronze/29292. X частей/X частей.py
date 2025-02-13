_,(*n,),(*X,)=[map(int,i.split()[::-1])for i in open(0)]
a=0
while X and n:
    X[-1]-=n.pop()
    if X[-1]<1:a-=X.pop()
print(-1 if X else a+sum(n))