N,*l=open(0)
print('Not Eyfa'[all(j[::2]==i==j[1::2]+'\n'for i,j in zip(l,l[int(N[:2]):]))*4:])