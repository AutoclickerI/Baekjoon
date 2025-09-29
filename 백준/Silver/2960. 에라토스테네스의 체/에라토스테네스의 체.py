N,K=map(int,input().split())
i=N+1
l=[0,0]+[1]*i
while K:
 if N<i:i=p=l.index(1)
 K-=l[i];l[i]=0;i+=p
print(i-p)