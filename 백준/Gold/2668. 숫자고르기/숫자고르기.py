*l,=map(int,open(0))
visited=[0]*len(l)
def DFS(n,start):
    if visited[n]:return n==start
    visited[n]=1
    return DFS(l[n],start)
for i in range(1,len(l)):
    tmp=visited[:]
    visited=DFS(i,i)*visited or tmp
print(sum(visited),*[i for i in range(len(l))if visited[i]])