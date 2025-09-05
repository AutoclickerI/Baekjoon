d={'M':[]}
e={'M':1}
def f(x,n):
 q=[x]
 for i in q:
  if e[i]: 
   if n<1:return i
   n-=1
  q+=d[i]
 return '-'
for i in[*open(0)][1:]:
 x,a,*y=i.split()
 if x=='-':e[a]=0
 if x=='+':d[a]+=y;d[y[0]]=[];e[y[0]]=1
 x=='?'!=print(f('M',int(a)-1))