n,m,*l=open(0).read().split()
g=int(m)-sum(map(len,l))
print(('No','Yes')[g>0 and not g%(int(n)-1) if int(n)>1 else not g])