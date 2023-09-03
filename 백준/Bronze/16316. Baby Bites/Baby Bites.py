n,*l=open(0).read().split()
print(['makes sense','something is fishy'][any({i}-{str(j+1),'mumble'}for i,j in zip(l,range(int(n))))])