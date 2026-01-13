[N,M,K],*l=[[*map(int,i.split())]for i in open(0)]

end=[-1]*-~M

def DFS(n):
    v[n]=1
    for e in l[n][1:]:
        if end[e]<0 or v[end[e]]<1 and DFS(end[e]):
            end[e]=n
            return 1
    return 0
for i in range(2*N):
    if K<1:
        break
    v=[0]*N
    if DFS(i%N):
        K-=N<=i
print(sum(-1<i for i in end))