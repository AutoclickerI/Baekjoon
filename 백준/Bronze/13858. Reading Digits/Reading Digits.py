i,e=open(0)
exec("e=''.join(j*int(i)for i,j in zip(*[iter(e)]*2));"*int(i[:2]))
print(e[int(i[2:])])