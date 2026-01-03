import sys
input=sys.stdin.readline

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

for T in[0]*int(input()):
    N=int(input())
    b=[[*map(int,input().split())]for _ in[0]*N]
    *p,=range(N)
    for i in range(N):
        x1,y1,r1=b[i]
        for j in range(i+1,N):
            x2,y2,r2=b[j]
            if (x1-x2)**2+(y1-y2)**2<=(r1+r2)**2:
                i,j=sorted(map(find,[i,j]))
                p[j]=i
    s=set()
    for i in range(N):
        s.add(find(i))
    print(len(s))