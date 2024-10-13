v=open(0)
next(v)
for x,y,z in zip(v,v,v):print(len(y)+min(x:=int(x),k:=sum(i==j for i,j in zip(y,z))-1)-max(k,x)-1)