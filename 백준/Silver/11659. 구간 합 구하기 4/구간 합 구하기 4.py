_,l,*z=map(str.split,open(0))
v=[0]
for i in l:v+=v[-1]+int(i),
for s,e in z:print(v[int(e)]-v[int(s)-1])