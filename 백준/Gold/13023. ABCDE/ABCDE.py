N,M=map(int,input().split())
l=[[]for _ in[0]*N]
for _ in[0]*M:
    s,e=map(int,input().split())
    l[s]+=e,
    l[e]+=s,

def DFS(n,depth,visited):
    if depth==4:
        return 1
    for i in l[n]:
        if i not in visited:
            if DFS(i,depth+1,visited|{i}):
                return 1
    return 0

for i in range(N):
    if DFS(i,0,{i}):
        print(1)
        break
else:
    print(0)