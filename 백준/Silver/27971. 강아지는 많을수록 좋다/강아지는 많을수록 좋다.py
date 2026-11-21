N,M,A,B,*L=map(int,open(0).read().split())
l=[0]+[-1]*N
while L:p,q,*L=L;l[p:q+1]=[-2]*(q-p+1)
for i in range(min(A,B),N+1):exec((l[i]!=-2)*'''p,q=l[i-A],l[i-B]
if p>-1<q:l[i]=min(p,q)+1
else:
 if p>=0:l[i]=p+1
 if q>=0:l[i]=q+1''')
print(max(-1,l[N]))