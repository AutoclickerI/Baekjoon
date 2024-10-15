s=[]
for i in[*open(0)][1:]:
 t,*l=i.split();v=[0,0,t]
 for x,y in zip(*[iter(l)]*2):
  if int(y):v[0]+=1;v[1]-=int(y)+20*(int(x)-1)
 s+=v,
x,y,z=sorted(s)[-1]
print(z,x,-y)