import sys
input=sys.stdin.readline

N,M=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]

for m in range(N):
    for s in range(N):
        for e in range(N):
            b[s][e]=min(b[s][e],b[s][m]+b[m][e])

for _ in[0]*M:
    A,B,C=map(int,input().split())
    if b[A-1][B-1]<=C:
        print('Enjoy other party')
    else:
        print('Stay here')