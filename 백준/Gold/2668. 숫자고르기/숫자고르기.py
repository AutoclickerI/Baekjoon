*l,=map(int,open(0))
V=[0]*len(l)
def DFS(n,s):
    if V[n]:return n==s
    V[n]=n;return DFS(l[n],s)
for i in range(1,len(l)):T=V[:];V=V*DFS(i,i)or T
print(len(S:=set(V))-1,*sorted(S)[1:])