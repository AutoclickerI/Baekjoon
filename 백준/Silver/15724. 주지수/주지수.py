import sys
input=sys.stdin.readline

N,M=map(int,input().split())
b=[[0]*-~M]
for _ in[0]*N:
    r=[0]
    for i,v in enumerate(input().split()):
        r+=r[-1]+int(v)+b[-1][i+1]-b[-1][i],
    b+=r,
for _ in[0]*int(input()):
    x1,y1,x2,y2=map(int,input().split())
    print(b[x2][y2]+b[x1-1][y1-1]-b[x2][y1-1]-b[x1-1][y2])