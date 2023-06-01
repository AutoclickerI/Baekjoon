from collections import deque
l=deque()
_,*p=open(0)
for L in p:
    L=L.split()
    try:
        if L[0]=='front':print(l[0])
        elif L[0]=='back':print(l[-1])
        elif L[0]=='size':print(len(l))
        elif L[0]=='empty':print(+(len(l)==0))
        elif L[0]=='pop_back':print(l.pop())
        elif L[0]=='push_back':l.append(L[1])
        elif L[0]=='pop_front':print(l.popleft())
        elif L[0]=='push_front':l.appendleft(L[1])
    except:print(-1)