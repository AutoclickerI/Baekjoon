from collections import*
l=deque()
_,*p=open(0)
for i in p:
 i=i.split();I=i[0][0]
 try:l.append(i[1])if i[0]=='push'else print(l[0]if I=='f'else l[-1]if I=='b'else len(l)if I=='s'else l.popleft()if I=='p'else 0if len(l)else 1)
 except:print(-1)