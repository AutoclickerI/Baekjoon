p=m=0
g,n,*l=map(int,open(0))
N,*a=n,
while n:x=l[p];p-=~x;a+=l[p-x:p],;n-=1
for i in range(g):
 W=0
 for j in a:
  w=l=0
  for k in j:
   if max(w:=w+2-k,l:=l+k-1)>i:W+=w>i;break
 if m<W>0<i+1<g:m=W;q=i+1
print(a[0].count(1),N-W,q)