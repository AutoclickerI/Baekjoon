_,q,*z=[[*map(int,i.split())]for i in open(0)]
l=[]
while z:v=z[0][0]+1;s,e=q[:2];l+=sum(abs(s-(s:=i))+abs(e-(e:=j))for i,j in(*z[1:v],q[2:])),;z=z[v:]
print(l.index(min(l))+1)