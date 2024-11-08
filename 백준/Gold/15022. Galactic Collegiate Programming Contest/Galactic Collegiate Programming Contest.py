import sys
input=sys.stdin.readline

from heapq import*

N,M=map(int,input().split())

hq=[]
d={i:[0,0,-i]for i in range(2,N+1)}
dup_cnt={}
cnt=0
v=[0,0,-1]
for _ in[0]*M:
    t,p=map(int,input().split())
    if t!=1:
        l=d[t][:]
        l[0]+=1
        l[1]-=p
        d[t]=l
        if v<l:
            if t not in dup_cnt:
                cnt+=1
                dup_cnt[t]=0
            dup_cnt[t]+=1
            heappush(hq,l)
    else:
        v[0]+=1
        v[1]-=p
        while hq and hq[0]<v:
            _,_,i=heappop(hq)
            dup_cnt[-i]-=1
            if dup_cnt[-i]==0:
                cnt-=1
                del dup_cnt[-i]
            
    print(cnt+1)