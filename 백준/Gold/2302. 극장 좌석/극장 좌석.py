N,M,*l=map(int,open(q:=0))
i=p=1
while i<=N:f=1-(i in l);p,q=p+q*f,p*f;i+=1
print(p)