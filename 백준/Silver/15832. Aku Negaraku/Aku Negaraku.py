from collections import*
while sum(l:=[*map(int,input().split())]):
 N,M=l;d=deque(range(N,0,-1))
 while~-len(d):d.rotate(M-1);d.pop()
 print(d[0])