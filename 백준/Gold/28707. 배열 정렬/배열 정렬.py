from heapq import*
n=int(input())
*l,=map(int,input().split())
sl=sorted(l)
change=[[*map(int,input().split())]for _ in[0]*int(input())]
hq=[(0,l)]
visited={tuple(l):0}
while hq:
    n,l=heappop(hq)
    for left,right,c in change:
        l[left-1],l[right-1]=l[right-1],l[left-1]
        if tuple(l) not in visited or n+c<visited[tuple(l)]:
            heappush(hq,(n+c,l[:]))
            visited[tuple(l)]=n+c
        l[left-1],l[right-1]=l[right-1],l[left-1]
print(visited.get(tuple(sl),-1))