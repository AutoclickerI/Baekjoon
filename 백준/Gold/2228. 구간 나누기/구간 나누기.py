n,m,*l=map(int,open(0).read().split())
c=[[0,0]]+[[-1e9]*2]*m
for i in l:c[1:]=[[max(c[j+1][0],c[j][1])+i,max(c[j+1])]for j in range(m)]
print(max(c[m]))