[N,s,e],*l=[map(int,i.split())for i in open(0)]
V=[1]*-~N
x=[[]for _ in V]
for p,q,v in l:x[p]+=(q,v),;x[q]+=(p,v),
l=[(s,0,0)]
for s,c,w in l:
 s==e<exit(print(w-c))
 for n,v in x[s]:l+=[(n,max(v,c),w+v)]*V[n];V[n]=0