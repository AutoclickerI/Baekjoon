k,*l=open(0)
k=int(k[2:])
for i in l:print(*sum([k*[c]for c in i[::2]],[])*k)