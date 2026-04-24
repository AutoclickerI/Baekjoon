n,k,*l=map(int,open(0).read().split())

r=0
s=0
for i in range(k):
    r-=l[i]*~i
    s+=l[i]
a=[(r,0)]
for i in range(n-k):
    r-=s
    s-=l[i]
    s+=l[i+k]
    r+=l[i+k]*k
    a+=(r,i+1),

for i,j in sorted(a):print(j+1,i)