N,*l=open(0)
l=[0,*zip(*l)]
t=*'X'*int(N.split()[0]),
print(l.index(t)if t in l else'ESCAPE FAILED')