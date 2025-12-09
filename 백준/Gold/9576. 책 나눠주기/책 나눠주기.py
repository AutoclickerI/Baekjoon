def DFS(i):
    v[i]=1
    p,q=l[i]
    for e in range(p,q+1):
        if end[e]<1 or v[end[e]-1]<1 and DFS(end[e]-1):
            start[i]=e
            end[e]=i+1
            return 1
    return 0
        

for T in[0]*int(input()):
    N,M=map(int,input().split())
    l=[[*map(int,input().split())]for _ in[0]*M]
    start=[0]*-~M
    end=[0]*-~N
    
    for i in range(M):
        v=[0]*-~M
        DFS(i)
    print(sum(0<i for i in end))