N,K,*l=map(int,open(0).read().split())
d=-~K*[0]
while l:
 w,v,*l=l
 for i in range(K,w-1,-1):d[i]=max(d[i],d[i-w]+v)
print(d[K])
