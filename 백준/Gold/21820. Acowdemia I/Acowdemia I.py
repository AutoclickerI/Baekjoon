N,L=map(int,input().split())
l=sorted(map(int,input().split()))
hindex=0
for i,j in zip(range(N),l[::-1]):
    if i<j:hindex=i+1
s=min(hindex+1,N)
while L and s:
    l[-s]+=1
    s-=1
    L-=1
hindex=0
for i,j in zip(range(N),sorted(l)[::-1]):
    if i<j:hindex=i+1
print(hindex)