N,S,*l=map(int,open(0).read().split())
l*=2
p=P=s=0
m=N=N+1
while P<N:
 while s<S:s+=l[P];P+=1
 m+=(min(m,P-p)-m)*(s>=S);s-=l[p];p+=1
print(m-N and m)