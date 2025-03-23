import sys
input=sys.stdin.readline

def bellman_ford(n):
    v=[9**9]*N
    v[n]=0
    for _ in[0]*n:
        for s,e,c in edges:
            v[e]=min(v[e],v[s]+c)
    return-1<v[n]

for _ in[0]*int(input()):
    N,M,W=map(int,input().split())
    b=[[9**9*(i!=j)for i in range(N)]for j in range(N)]
    edges=[]
    for _ in[0]*M:
        s,e,c=map(int,input().split())
        edges+=(s-1,e-1,c),(e-1,s-1,c)
    se=set()
    for _ in[0]*W:
        s,e,c=map(int,input().split())
        edges+=(s-1,e-1,-c),
        se|={e-1,s-1}
    print('YNEOS'[all(map(bellman_ford,se))::2])