from collections import*
while'1'<(s:=input()):
 N,M=map(int,s.split());d=deque(range(N))
 while~-len(d):d.rotate(M-1);d.pop()
 print(N-d[0])