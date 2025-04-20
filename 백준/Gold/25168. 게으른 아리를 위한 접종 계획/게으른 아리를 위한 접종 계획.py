d=[1]*6**6
for s,e,m in sorted([[*map(int,i.split())]for i in open(0)][1:]):d[e]=max(d[e],d[s]+m+(6<m))
print(max(d))