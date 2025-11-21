n=int(input())+1
m=int(input())

b=[n*[float('inf')]for _ in[0]*n]
v=[[[]for _ in[0]*n]for _ in[0]*n]

for i in range(n):b[i][i]=0;

for _ in[0]*m:
    s,e,r=map(int,input().split())
    if r<b[s][e]:
        v[s][e]=[s,e]
        b[s][e]=r

for m in range(n):
    for s in range(n):
        for e in range(n):
            if b[s][m]+b[m][e]<b[s][e]:
                b[s][e]=b[s][m]+b[m][e]
                v[s][e]=v[s][m]+v[m][e][1:]

for y in range(1,n):
    for x in range(1,n):
        print(0 if b[y][x]==float('inf')else b[y][x],end=' ')
    print()

for ss in range(1,n):
    for e in range(1,n):
        s=ss
        ret=v[s][e]
        print(len(ret),end=' ')
        print(*ret)