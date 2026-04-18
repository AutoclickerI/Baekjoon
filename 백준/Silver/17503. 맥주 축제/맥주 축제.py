from heapq import*
[K,M,N],*l=[[*map(int,i.split())][::-1]for i in open(0)]
hq=[]
s=0
for c,v in sorted(l):
    heappush(hq,v)
    s+=v
    if len(hq)==N:
        M<=s<exit(print(c))
        s-=heappop(hq)
print(-1)