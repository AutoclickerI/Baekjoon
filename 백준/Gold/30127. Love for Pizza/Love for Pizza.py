import math

cmp=lambda i:math.atan2(*i[1:])

for _ in[0]*int(input()):
    N=int(input())
    r,*l=sorted([[*map(int,input().split())]for _ in[0]*N],key=cmp)
    r=[r]
    for i in l:
        if abs(cmp(r[-1])-cmp(i))<1e-6:
            r[-1][0]+=i[0]
        else:
            r+=i,
    vm=vM=0
    mM=-float('inf')
    mm=float('inf')
    l=[i for i,*_ in r]
    for i in l:
        vm=min(vm,0)+i
        vM=max(vM,0)+i
        mm=min(mm,vm)
        mM=max(mM,vM)
    print(max(mM,sum(l)-mm))