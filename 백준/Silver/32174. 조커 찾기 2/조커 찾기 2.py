N,M=map(int,input().split())
l=[1]
for _ in[0]*M:
    a,b=map(int,input().split())
    if a==1:
        l+=(l[-1]+b-1)%N+1,
    if a==2:
        l+=(l[-1]-b-1)%N+1,
    if a==3:
        l+=l[b],
print(l[-1])