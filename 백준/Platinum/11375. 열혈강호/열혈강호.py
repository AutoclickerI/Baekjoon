N,M=map(int,input().split())
end=[0]*(M+1)
node=[0]
for _ in[0]*N:
    node+=[[*map(int,input().split()[1:])]]
def DFS(n):
    V[n]=1
    for i in node[n]:
        if 0==end[i]or~-V[end[i]]and DFS(end[i]):
            end[i]=n
            return 1
    return 0
a=0
for i in range(1,N+1):
    V=[0]*(N+1)
    a+=DFS(i)
print(a)