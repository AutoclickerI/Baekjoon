from heapq import*
input()
*minheap,=map(int,input().split())
heapify(minheap)
origmax=nowmax=max(minheap)
ans=origmax-minheap[0]
while minheap[0]!=origmax:
    ans=min(ans,nowmax-minheap[0])
    n=heappop(minheap)
    n*=2
    nowmax=max(nowmax,n)
    heappush(minheap,n)
print(min(ans,nowmax-minheap[0]))