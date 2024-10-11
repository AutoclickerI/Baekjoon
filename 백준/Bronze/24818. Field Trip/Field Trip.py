from bisect import*

n,*l=map(int,open(0).read().split())

for i in range(1,n):l[i]+=l[i-1]

if l[-1]%3:print(-1)
else:
    p=l[-1]//3
    s,i=bisect_right(l,p),bisect_left(l,p)
    t,j=bisect_right(l,2*p),bisect_left(l,2*p)
    if s-i==1==t-j:print(i+1,j+1)
    else:print(-1)