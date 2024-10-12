from collections import deque
N,K=map(int,input().split())
dq=deque(range(1,N+1))
while 1:
    s=dq.popleft()
    for _ in[0]*~-K:
        if dq:
            dq.popleft()
        else:
            break
    else:
        dq+=s,
        continue
    break
print(s)