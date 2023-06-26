from collections import deque
dq=deque()
for i in[*open(0)][1:]:
    p,*q=map(int,i.split())
    if p==1:dq.appendleft(q[0])
    elif p==2:dq.append(q[0])
    elif p==5:print(len(dq))
    elif p==6:print(1-bool(dq))
    else:
        try:
            if p==3:v=dq.popleft()
            if p==4:v=dq.pop()
            if p==7:v=dq[0]
            if p==8:v=dq[-1]
            print(v)
        except:print(-1)