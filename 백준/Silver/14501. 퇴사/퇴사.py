d=[r:=0]*30
for i in[*open(0)][1:]:d[t]=max(d[t:=int(i[0])],r+int(i[1:]));_,*d=d;r=max(r,d[0])
print(r)