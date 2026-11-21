_,*l=[[*map(int,i.split())]for i in open(0)]
for x,y,r in l:print(sum((p-x)**2+(q-y)**2<=(r+z)**2for p,q,z in l)-1)