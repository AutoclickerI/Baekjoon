from collections import deque
l=deque()
_,*p=open(0)
for i in p:
    i=i.split()
    I=i[0]
    try:l.append(i[1])if I=='push'else print(l[0]if I=='front'else l[-1]if I=='back'else len(l)if I=='size'else l.popleft()if I=='pop'else 0 if len(l)else 1)
    except:print(-1)