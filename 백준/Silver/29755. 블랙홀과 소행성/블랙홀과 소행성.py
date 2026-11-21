import sys
from bisect import*
inpupt=sys.stdin.readline
N,M=map(int,input().split())
l=sorted(map(int,input().split()))
P=0
for _ in[0]*M:
    a,w=map(int,input().split())
    b=bisect_left(l,a)
    if b!=0:
        if b==len(l):
            b=abs(l[b-1]-a)
        else:
            b=min(abs(l[b]-a),abs(l[b-1]-a))
    else:
        b=abs(l[b]-a)
    P=max(P,b*w)
print(P)