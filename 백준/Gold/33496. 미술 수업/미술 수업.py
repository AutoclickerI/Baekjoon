import sys
input=sys.stdin.readline

from bisect import bisect_left

p=set()
q=set()
for _ in[0]*int(input()):
    X,Y=map(int,input().split())
    p|={X-Y}
    q|={X+Y}
a=len(p)+len(q)-len(p&q)
p=sorted(p)
for i in sorted(q):
    a+=bisect_left(p,i)
print(a)