(N,M),*l=[[*map(int,i.split())]for i in open(0)]
d=[1]*-~N
for s,e,m in sorted(l):d[e]=max(d[e],d[s]+m+(6<m))
print(max(d))