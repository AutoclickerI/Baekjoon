import sys
input=sys.stdin.readline
d={}
P,Q=map(int,input().split())
for _ in[0]*P:p,q=input().split();d[p]=q
for _ in[0]*Q:print(d[input().strip()])