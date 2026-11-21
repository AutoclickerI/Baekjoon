n,*l=[eval(i.replace(' ','+1j*'))for i in open(0)]
print(sum(l:=[abs(j-i)for i,j in zip(l,l[1:]+l)])-max(l))