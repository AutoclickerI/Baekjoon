def f(n):
 if n-v[n]:v[n]=f(v[n])
 return v[n]
(N,M),*l=[map(int,i.split())for i in open(0)]
*v,=range(N+1)
for p,i,j in l:
 i,j=sorted([f(i),f(j)])
 if p:print('YNEOS'[i<j::2])
 else:v[i]=j