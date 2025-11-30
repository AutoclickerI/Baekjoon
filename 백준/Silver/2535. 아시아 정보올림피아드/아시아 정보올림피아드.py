v,*r=[0]*999,
for s,n,c in sorted([[*map(int,i.split())][::-1]for i in open(0)][1:])[::-1]:f=v[c]<2;v[c]+=f;r+=[(c,n)]*f
for i in r[:3]:print(*i)