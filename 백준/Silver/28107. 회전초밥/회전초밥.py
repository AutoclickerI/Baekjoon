(N,M),*x,z=[[*map(int,i.split())]for i in open(0)]
l=[[]for _ in[0]*8**6]
c=[v:=0]*N
while v<N:
 for i in x[v][1:]:l[i]+=v,
 v+=1
l=[i[::-1]for i in l]
for i in z:
 if l[i]:c[l[i].pop()]+=1
print(*c)