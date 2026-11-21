_,a,*q=[map(int,s.split())for s in open(0)]
a=[0,*a]
for s,t,u in q:
 if~-s:print(abs(a[t]-a[u]))
 else:a[t]=u