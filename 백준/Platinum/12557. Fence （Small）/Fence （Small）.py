import sys
input=sys.stdin.readline

from heapq import*

for T in range(int(input())):
    M,N=map(int,input().split())
    *A,=map(int,input().split())
    A.sort()
    
    C=A.pop()
    v=[float('inf')]*C
    v[0]=0
    
    hq=[(0,0)]
    
    while hq:
        c,n=heappop(hq)
        if v[n]<c:
            continue
        for i in A:
            nn=(n+C-i)%C
            if c+C-i<v[nn]:
                v[nn]=c+C-i
                heappush(hq,(c+C-i,nn))
    v=(M+v[-M%C])//C
    print(f'Case #{T+1}:',['IMPOSSIBLE',v][type(v)==int])