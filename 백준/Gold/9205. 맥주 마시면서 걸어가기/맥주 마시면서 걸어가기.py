for _ in[0]*int(input()):
    n=int(input())
    l=[[*map(int,input().split())]for _ in[0]*(n+2)]
    edges=[[]for _ in[0]*(n+2)]
    for i in range(n+2):
        for j in range(i+1,n+2):
            if abs(l[i][0]-l[j][0])+abs(l[i][1]-l[j][1])<=1000:
                edges[i]+=j,
                edges[j]+=i,
    visited=[0]*(n+2)
    v=[0]
    for n in v:
        for e in edges[n]:
            if visited[e]<1:
                visited[e]=1
                v+=e,
    print('happy'*visited[-1]or'sad')