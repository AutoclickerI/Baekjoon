n=int(input())
v=set()
for i in map(int,input().split()):
    v.add(i)
def DFS(n):
    if n in v:
        return 0
    else:
        return DFS(2*n)+DFS(2*n+1)+1
try:
    x=DFS(1)
except:
    x=-1
print(x)