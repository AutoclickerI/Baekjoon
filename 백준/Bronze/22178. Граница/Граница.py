s=open(0).read().split()[2:]
print(sum(sum(map(str.__ne__,i,i[1:]))for i in[*zip(*s)]+s))