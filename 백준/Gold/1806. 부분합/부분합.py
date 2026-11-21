N,S,*l=map(int,open(0).read().split())
l*=2
p=P=s=0
m=N=N+1
while P<N:
 while s<S:s+=l[P];P+=1
 if s>=S:m=min(m,P-p)
 s-=l[p];p+=1
print(m-N and m)