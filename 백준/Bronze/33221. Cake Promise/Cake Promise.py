X=1e9
_,t,*l=[eval(s.replace(*' +'))for s in open(0)]
print(sum(i<=t for i in l))