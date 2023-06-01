import sys
from heapq import*
input=sys.stdin.readline
for _ in range(int(input())):
    maxheap=[]
    minheap=[]
    for _ in range(int(input())):
        c,i=input().split()
        if c=='I':
            checker=[1]
            heappush(minheap,[int(i),checker])
            heappush(maxheap,[-int(i),checker])
        else:
            try:
                if i=='1':
                    l=heappop(maxheap)
                    while l[1][0]==0:
                        l=heappop(maxheap)
                    l[1][0]=0
                else:
                    l=heappop(minheap)
                    while l[1][0]==0:
                        l=heappop(minheap)
                    l[1][0]=0
            except:0
    try:
        maxval=heappop(maxheap)
        while maxval[1][0]==0:
            maxval=heappop(maxheap)
        minval=heappop(minheap)
        while minval[1][0]==0:
            minval=heappop(minheap)
        print(-maxval[0],minval[0])
    except:
        print('EMPTY')