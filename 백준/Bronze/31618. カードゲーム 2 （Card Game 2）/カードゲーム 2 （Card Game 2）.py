l=[0]*200001
for i in map(int,[*open(0)][1].split()):l[i]=1
for i,j,k in zip(l,l[3:],l[6:]):i*j*k>0<exit(print('Yes'))
print('No')