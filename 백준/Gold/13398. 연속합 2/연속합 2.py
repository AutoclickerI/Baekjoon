v,*l=map(int,[*open(s:=0)][1].split())
m=v
for i in l:
    v,s=max(v+i,i),max(v,s+i,i)
    m=max(m,v,s)
print(m)