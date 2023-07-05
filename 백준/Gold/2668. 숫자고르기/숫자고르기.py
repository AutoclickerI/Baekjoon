*l,=map(int,open(0))
ans=set()
def DFS(n,start):
    if visited[n]:
        if n!=start:return
        for i in range(len(l)):
            if visited[i]:ans.add(i)
        return 1
    visited[n]=1
    DFS(l[n],start)
for i in range(1,len(l)):
    visited=[0]*len(l)
    DFS(i,i)
print(len(ans),*sorted(ans))