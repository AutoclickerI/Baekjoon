_,p,_,q=open(0)
d={}
for i in p.split():d[i]=d.get(i,0)+1
for i in q.split():print(d.get(i,0))