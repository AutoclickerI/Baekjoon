_,c,*l=[[0,*map(int,i.split())]for i in open(0)]
for i in l:
 k=-1
 for v in i:
  if c[v]:c[k:=v]-=1;break
 print(k)