from collections import*
while sum(l:=[*map(int,input().split())]):
 N,M=l;d=deque(range(1,N+1))
 while len(d)>1:d.rotate(1-M);d.popleft()
 print(d[0])