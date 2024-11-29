n,m=map(int,input().split())
l=[]
for _ in[0]*n:
    tmp=[0]
    for i in map(int,input().split()):
        tmp+=tmp[-1]+i,
    l+=[(j,i)for i,j in enumerate(tmp)]
l.sort()

ans=[0]*-~m
cur=[0]*(m+2)
cur[0]=n
prev=0
for t,idx in l:
    if t!=prev:
        for i in range(-~m):
            ans[i]=max(ans[i],cur[i])
    cur[idx]-=1
    cur[idx+1]+=1
    prev=t
print(*ans[1:])