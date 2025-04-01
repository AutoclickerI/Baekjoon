m=v=p=0
for i in[*open(0)][1].split():m=max(m,v:=max(0,v+p-(p:=int(i))))
print(m)