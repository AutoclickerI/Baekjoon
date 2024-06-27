import sys
input=sys.stdin.readline
from heapq import*
for T in range(int(input())):
    N,M=map(int,input().split())
    c=sorted(eval('[*map(int,input().split())],'*M))
    orig=sum(k*(2*N*(j-i)-(j-i)*(j-i-1))for i,j,k in c)//2%1000002013
    v=0
    on=[]
    off=[]
    ptr=0
    while ptr<len(c):
        if c[ptr][0]==c[ptr][1]:
            ptr+=1
            continue
        heappush(off,c[ptr][1:])
        while off and off[0][0]<c[ptr][0]:
            s,kon=heappop(on)
            s=-s
            e,koff=heappop(off)
            v+=(2*N*(e-s)-(e-s-1)*(e-s))*min(koff,kon)
            if 0<koff-kon:
                heappush(off,[e,koff-kon])
            elif 0<kon-koff:
                heappush(on,[-s,kon-koff])
        heappush(on,[-c[ptr][0],c[ptr][2]])
        ptr+=1
    while off:
        s,kon=heappop(on)
        s=-s
        e,koff=heappop(off)
        v+=(2*N*(e-s)-(e-s-1)*(e-s))*min(koff,kon)
        if 0<koff-kon:
            heappush(off,[e,koff-kon])
        elif 0<kon-koff:
            heappush(on,[-s,kon-koff])
    print(f'Case #{T+1}:',(orig-v//2)%1000002013)