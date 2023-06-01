import sys
input=sys.stdin.readline
N,M=map(int,input().split())
l=[0,*map(int,input().split())]
for i in range(N):
    l[i+1]+=l[i]
for _ in[0]*M:
    p,q=map(int,input().split())
    print(l[q]-l[p-1])