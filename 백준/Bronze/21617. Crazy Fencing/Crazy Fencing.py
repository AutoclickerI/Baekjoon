_,l,x=[[*map(int,i.split())]for i in open(0)]
print(sum(k*(i+j)for i,j,k in zip(l,l[1:],x))/2)