d={'A':2,'R':1,'K':1,'T':1,'S':1}
for i in[*open(0)][c:=1]:d[i]=(d.get(i)or 1)-1;c+=any(d.values())
print(c)