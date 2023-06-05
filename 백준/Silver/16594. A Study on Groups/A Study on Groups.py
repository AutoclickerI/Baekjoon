n,m=map(int,input().split())
l=sorted(map(int,input().split()))
mi=sum(l[:m])
p=n//m
ma=0
s=0
for _ in[0]*(n-p*m):
    ma+=min(l[s:s+p+1])
    s+=p+1
while s!=n:
    ma+=min(l[s:s+p])
    s+=p
print(mi,ma)