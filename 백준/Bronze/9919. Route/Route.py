g=lambda c:c and(c>0)*2-1
n,*a=map(int,open(0).read().split())
r=[0,0,0]
p=[g(a[i+1-n]-a[i])for i in range(n)]
r[p[0]]+=1
for i,j in zip(p,p[1:]):r[j]+=j!=i
print(*r)