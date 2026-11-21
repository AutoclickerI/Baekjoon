d={}
f=sorted
for x in f(open(0))[1:]:s,t=x.split();d[s]=d.get(s,0)+int(t)
for p in f(d,key=len):print(p,d[p])