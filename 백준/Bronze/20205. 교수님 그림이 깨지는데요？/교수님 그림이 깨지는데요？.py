k,*l=open(0)
k=int(k[2:])
for i in l:print(*''.join(c*k for c in i[::2])*k)