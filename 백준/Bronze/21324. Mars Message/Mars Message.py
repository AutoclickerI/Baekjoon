N,*l=map(eval,open(0))
for i,j in zip(*[iter(l)]*2):print(end=chr(int((i//22.5))*16+int(j//22.5)))