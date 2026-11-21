N,M=map(int,input().split())
S=int(input())
d={}

from collections import deque

dq=deque()
cnt=0
forgot=[]

for _ in[0]*M:
    i,t=map(int,input().split())
    if t==0:
        d[i]=1
        cnt+=1
        while dq and dq[0][0]+S<=cnt:
            _,n=dq.popleft()
            if n not in d:
                forgot+=n,
    else:
        dq+=(cnt,i),

if forgot:
    for i in sorted(forgot):print(i)
else:
    print(-1)