import sys
from heapq import*
input=sys.stdin.readline
for _ in range(int(input())):
    maxheap=[]
    minheap=[]
    d={}
    for _ in range(int(input())):
        c,i=input().split()
        if c=='I':
            checker=[1]
            heappush(minheap,int(i))
            heappush(maxheap,-int(i))
            d[int(i)]=d.get(int(i),0)+1
        else:
            try:
                if i=='1':
                    l=-heappop(maxheap)
                    while not d[l]:
                        l=-heappop(maxheap)
                    d[l]=max(0,d[l]-1)
                else:
                    l=heappop(minheap)
                    while not d[l]:
                        l=heappop(minheap)
                    d[l]=max(0,d[l]-1)
            except:0
    try:
        maxval=heappop(maxheap)
        while not d[-maxval]:
            maxval=heappop(maxheap)
        minval=heappop(minheap)
        while not d[minval]:
            minval=heappop(minheap)
        print(-maxval,minval)
    except:
        print('EMPTY')