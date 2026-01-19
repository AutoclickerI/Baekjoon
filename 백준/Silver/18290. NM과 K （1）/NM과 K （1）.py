import sys
sys.setrecursionlimit(2*10**5)
[N,M,K],*b=[[*map(int,i.split())]for i in open(0)]

l=[]
v=[M*[0]for _ in[0]*N]

def backtrack(n,c,r):
    if c<1 or n==N*M:
        if c<1:
            l.append(r)
        return
    backtrack(n+1,c,r)
    y,x=n//M,n%M
    if(y<1 or v[y-1][x]<1)and(x<1 or v[y][x-1]<1):
        v[y][x]=1
        backtrack(n+1,c-1,r+b[y][x])
        v[y][x]=0
backtrack(0,K,0)
print(max(l))