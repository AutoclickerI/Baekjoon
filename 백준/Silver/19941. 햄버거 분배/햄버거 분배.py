N,K=map(int,input().split())
s=input()
c=0
from collections import*
dq_h=deque()
dq_p=deque()
for i in range(N):
    if s[i]=='H':
        f=0
        while dq_p:
            n=dq_p.popleft()
            if i-n<=K:
                f=1
                break
        if f:
            c+=1
        else:
            dq_h+=i,
    else:
        f=0
        while dq_h:
            n=dq_h.popleft()
            if i-n<=K:
                f=1
                break
        if f:
            c+=1
        else:
            dq_p+=i,
print(c)