_,l,*z=map(str.split,open(s:=0))
v=[s:=s+int(i)for i in[0]+l]
for s,e in z:print(v[int(e)]-v[int(s)-1])