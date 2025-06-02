from bisect import*
n,*a=map(int,open(0).read().split())
d=[]
r=[]
for e in a:p=bisect(d,e-1);d[p:p+1]=e,;r+=p,
m,*t=max(r),
while n:n-=1;f=r[n]==m;t+=[n]*f;m-=f
print(len(d),*[a[i]for i in t[::-1]])