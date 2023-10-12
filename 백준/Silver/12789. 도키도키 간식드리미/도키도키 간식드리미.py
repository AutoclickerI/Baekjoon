from collections import deque
dq=deque()
input()
head=1
for i in map(int,input().split()):
    while dq:
        n=dq.pop()
        if n!=head:
            dq.append(n)
            break
        head+=1
    if i==head:
        head+=1
    else:
        dq.append(i)
while dq:
    n=dq.pop()
    if n!=head:
        dq.append(n)
        break
    head+=1
if dq:
    print('Sad')
else:
    print('Nice')