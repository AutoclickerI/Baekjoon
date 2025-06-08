n,*l=open(0)
n=int(n)
for s,_ in l[n+1:]:print(end={s:e for s,_,e,_ in l[:n]}.get(s,s))