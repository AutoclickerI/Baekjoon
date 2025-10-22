N,M,R=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]

v=[M*[0]for _ in[0]*N]
n,m=N,M
o=0
while n*m:
    for _ in[0]*(R%(2*n+2*m-4)):
        for i in range(m-1):
            v[o][o+i]=b[o][o+i+1]
            v[N-o-1][o+i+1]=b[N-o-1][o+i]
        for i in range(n-1):
            v[o+i][M-o-1]=b[o+i+1][M-o-1]
            v[o+i+1][o]=b[o+i][o]
        for i in range(m-1):
            b[o][o+i+1]=v[o][o+i+1]
            b[N-o-1][o+i]=v[N-o-1][o+i]
        for i in range(n-1):
            b[o+i+1][M-o-1]=v[o+i+1][M-o-1]
            b[o+i][o]=v[o+i][o]
        
    n-=2
    m-=2
    o+=1
for i in b:print(*i)