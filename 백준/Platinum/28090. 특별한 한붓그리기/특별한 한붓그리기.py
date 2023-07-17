N,_,*l=map(int,open(0).read().split())
node=[[]for _ in[0]*N]
match=[-1]*N
while l:p,q,*l=l;node[p-1]+=[q-1]
def DFS(n):
    if V[n]:return
    V[n]=1
    for i in node[n]:
        if match[i]==-1 or DFS(match[i]):
            match[i]=n
            return 1
for i in range(N):
    V=[0]*N
    if not DFS(i):exit(print('Newbie'))
print('Oldbie')