import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
N=int(input())
l=[set()for _ in range(N+1)]
visited=[1]+[0]*N
for _ in[0]*(N-1):
    a,b=map(int,input().split())
    l[a].add(b)
    l[b].add(a)
p,*ans=map(int,input().split())
i=0
def DFS(pos):
    global i
    visited[pos]=1
    while 1:
        if i==N-1:
            return
        n=ans[i]
        if not visited[n]:
            if n in l[pos]:
                i+=1
                DFS(n)
                continue
        break
p!=1 or DFS(1)
print(+all(visited))