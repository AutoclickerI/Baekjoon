n,*l=open(0)
n=int(n)
d={}
for s,_,e,_ in l[:n]:d[s]=e
for s,_ in l[n+1:]:print(end=d.get(s,s))