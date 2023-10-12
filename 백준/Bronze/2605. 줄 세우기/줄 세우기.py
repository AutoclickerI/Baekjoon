_,L,*l=open(i:=0)
for j in L.split():l.insert(i-int(j),i:=i+1)
print(*l)