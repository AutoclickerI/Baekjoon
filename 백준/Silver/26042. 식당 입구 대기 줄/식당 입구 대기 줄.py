r=(0,0)
from collections import*
dq=deque()
for i in[*open(0)][1:]:
    q,*v=i.split()
    if q=='1':
        dq+=v
        r=max(r,(len(dq),-int(dq[-1])))
    else:dq.popleft()
print(r[0],-r[1])