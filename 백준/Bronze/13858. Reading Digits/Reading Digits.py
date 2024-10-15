k,p,e=open(0).read().split()
exec("e=''.join(j*int(i)for i,j in zip(*[iter(e)]*2));"*int(k))
print(e[int(p)])