from collections import deque
l=deque()
for i in[*open(0)][1:]:
    p,*q=i.split()
    if p=='push':l.append(q[0])
    if p=='front':
        if len(l):
            print(n:=l.popleft())
            l.appendleft(n)
        else:print(-1)
    if p=='back':
        if len(l):
            print(n:=l.pop())
            l.append(n)
        else:print(-1)
    if p=='size':print(len(l))
    if p=='empty':print(1-min(len(l),1))
    if p=='pop':
        if len(l):
            print(n:=l.popleft())
        else:print(-1)