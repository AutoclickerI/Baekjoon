N,M,K=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]

p=[[*map(int,input().split())]for _ in[0]*K]

def rot(arr,r,c,s):
    y=r-s-1
    x=c-s-1
    N=M=2*s+1
    b=[[*i]for i in arr]
    v=[M*[0]for _ in[0]*N]
    n,m=N,M
    o=0
    while 1<n and 1<m:
        for i in range(m-1):
            v[o][o+i+1]=b[y+o][x+o+i]
            v[N-o-1][o+i]=b[y+N-o-1][x+o+i+1]
        for i in range(n-1):
            v[o+i+1][M-o-1]=b[y+o+i][x+M-o-1]
            v[o+i][o]=b[y+o+i+1][x+o]
        for i in range(m-1):
            b[y+o][x+o+i+1]=v[o][o+i+1]
            b[y+N-o-1][x+o+i]=v[N-o-1][o+i]
        for i in range(n-1):
            b[y+o+i+1][x+M-o-1]=v[o+i+1][M-o-1]
            b[y+o+i][x+o]=v[o+i][o]
            
        n-=2
        m-=2
        o+=1
    return b
m=1e9

from itertools import*

for i in permutations(p):
    arr=[[*i]for i in b]
    for j in i:
        arr=rot(arr,*j)
    m=min(m,min(sum(i)for i in arr))

print(m)