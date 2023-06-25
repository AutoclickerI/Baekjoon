import sys
input=lambda:sys.stdin.readline().strip()
N,M=map(int,input().split())
d={}
for _ in[0]*N:
    s=input()
    if len(s)>=M:d[s]=d.get(s,0)+1
def compare(a,b):
    if d[a]==d[b]:
        if len(a)==len(b):
            return (a>b)*2-1
        else:
            return (len(a)<len(b))*2-1
    else:
        return (d[a]<d[b])*2-1
from functools import cmp_to_key
print(*sorted(d, key=cmp_to_key(compare)))