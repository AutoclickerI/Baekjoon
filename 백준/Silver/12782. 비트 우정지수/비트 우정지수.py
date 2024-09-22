for i in[*open(0)][1:]:
 t=[0,0]
 for a,b in zip(*i.split()):t[int(a)]+=a!=b
 print(max(t))