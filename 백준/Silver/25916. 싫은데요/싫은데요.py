n,m,*a=map(int,open(0).read().split())
r=w=i=j=0
while j<n:
 w+=a[j]
 while w>m:w-=a[i];i+=1
 r=max(r,w);j+=1
print(r)