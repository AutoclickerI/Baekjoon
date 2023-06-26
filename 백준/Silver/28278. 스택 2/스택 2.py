from collections import deque
dq=deque()
for i in[*open(0)][1:]:
    p,*q=map(int,i.split())
    if p==1:dq.append(q[0])
    elif p==3:print(len(dq))
    elif p==4:print(1-bool(dq))
    else:
        try:
            if p==2:v=dq.pop()
            if p==5:v=dq[-1]
            print(v)
        except:print(-1)