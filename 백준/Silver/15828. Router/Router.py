N,*l,_=map(int,open(0))
from collections import deque
dq=deque()
acc=0
for i in l:
    if i<1:
        acc-=1
        dq.popleft()
    elif acc+1<N:
        dq+=i,
        acc+=1
print(*dq or['empty'])