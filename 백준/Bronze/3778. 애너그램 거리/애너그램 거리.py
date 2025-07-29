next(x:=open(T:=0))
for[*a],[*b]in zip(x,x):
 T+=1
 for e in*a,:
  if e in b:b.remove(e);a.remove(e)
 print('Case #%d:'%T,len(a+b))