f=lambda:[*map(int,input().split())]
while(l:=f())[0]:
 m,n,p=l;P=[0]*-~m;P[p]=1
 for i in range(n):v,w=f();P[v]=P[w]=P[v]|P[w]
 print(sum(P))