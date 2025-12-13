import sys
sys.setrecursionlimit(10**5)

[N,M],*l=[[*map(int,i.split())]for i in open(0)]
end=[-1]*M
l*=2
N*=2
def DFS(n):
    v[n]=1
    for e in l[n][1:]:
        e-=1
        if end[e]<0 or(v[end[e]]<1 and DFS(end[e])):
            end[e]=n
            return 1
    return 0

for i in range(N):
    v=[0]*N
    DFS(i)
print(sum(-1<i for i in end))