l=[[*map(int,i.split())]for i in open(0)]
s='%3d '*3
for i in l[16:]:print((s+'maps to '+s)%(*i,*min(l[:16],key=lambda j:sum((v-w)**2for v,w in zip(i,j)))))