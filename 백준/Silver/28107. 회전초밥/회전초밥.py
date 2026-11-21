(N,M),*x,z=[[*map(int,i.split())]for i in open(0)]
l=[[]for _ in[0]*8**6]
for v in range(N):
 for i in x[v][1:]:l[i]+=v,
l=[i[::-1]for i in l]
c=[0]*N
for i in z:
 if l[i]:c[l[i].pop()]+=1
print(*c)