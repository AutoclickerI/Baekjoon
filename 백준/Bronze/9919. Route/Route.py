g=lambda c:c and c//abs(c)
n,*a=map(int,open(0).read().split())
a+=a[0],
r=[0,0,0]
p=[g(a[i+1]-a[i])for i in range(n)]
r[p[0]]+=1
for i in range(1,n):r[p[i]]+=p[i]!=p[i-1]
print(*r)