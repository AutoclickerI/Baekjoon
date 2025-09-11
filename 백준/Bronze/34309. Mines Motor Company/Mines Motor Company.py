_,*l=open(0,'rb')
print(sum(abs(i-j)for k in zip(l,l[1:])for i,j in zip(*k)))