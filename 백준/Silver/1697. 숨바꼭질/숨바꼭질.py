N,K=map(int,input().split())
visited=[0]*200001

from collections import deque

visited[N]=1
dq=deque([(0,N)])

while dq:
    time,pos=dq.popleft()
    if pos==K:
        break
    for next_pos in pos-1,pos+1,pos*2:
        if 0<=next_pos<200001 and visited[next_pos]<1:
            visited[next_pos]=1
            dq.append((time+1,next_pos))
print(time)