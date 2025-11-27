u=5,3,4,1,2,0
[N],*d=[[*map(int,i.split())]for i in open(0)]
for r in d[p:=0]:
 s=0
 for i in d:s+=max(i[j]*(u[k:=i.index(r)]!=j!=k)for j in u);r=i[u[k]]
 p=max(s,p)
print(p)