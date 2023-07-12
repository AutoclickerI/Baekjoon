import sys
input=sys.stdin.readline
n=int(input())
l=sorted(map(int,input().split()))
from collections import deque
ans1=ans2=ans3=ans4=0
dq=deque(l)
s=dq.popleft()
arr=[s]
while dq:
    tmp=dq.pop()
    ans1+=abs(s-tmp)
    s=tmp
    arr+=[tmp]
    if dq:
        tmp=dq.popleft()
        ans1+=abs(s-tmp)
        s=tmp
        arr+=[tmp]
dq=deque(arr)
s=dq.pop()
while dq:
    tmp=dq.popleft()
    ans2+=abs(s-tmp)
    s=tmp
dq=deque(l)
s=dq.pop()
arr=[s]
while dq:
    tmp=dq.popleft()
    ans3+=abs(s-tmp)
    s=tmp
    arr+=[tmp]
    if dq:
        tmp=dq.pop()
        ans3+=abs(s-tmp)
        s=tmp
        arr+=[tmp]
dq=deque(arr)
s=dq.pop()
while dq:
    tmp=dq.popleft()
    ans4+=abs(s-tmp)
    s=tmp
print(max(ans1,ans2,ans3,ans4))