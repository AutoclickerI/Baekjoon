from collections import deque
dq=deque()
n,b,a=map(int,input().split())
l=sorted(map(int,input().split()))
ans=0
for i in range(a):
    dq.append(l[i]//2)
    b-=l[i]//2
    if b<0:
        exit(print(ans))
    ans+=1
for i in range(a,n):
    dq.append(l[i]//2)
    b-=dq.popleft()+l[i]//2
    if b<0:
        exit(print(ans))
    ans+=1
print(ans)