from collections import*
N=int(input())
d=deque()
exec('d.appendleft(N);d.rotate(N);N-=1;'*N)
print(*d)