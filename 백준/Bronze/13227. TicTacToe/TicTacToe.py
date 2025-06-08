a,b,c=open(0).read().split()
print('NYOE S'[any({*i}<{'X','O'}for i in[a,b,c,*zip(a,b,c),(a[0],b[1],c[2]),(a[2],b[1],c[0])])::2])