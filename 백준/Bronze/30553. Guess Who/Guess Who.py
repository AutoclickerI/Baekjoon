n,m,q=map(int,input().split())
t=eval('input(),'*n)
*r,=range(n)
for _ in[0]*q:
 a,b=input().split();q=set()
 for i in r:
  if t[i][int(a)-1]==b:q|={i}
 r=q
if len(r)<2:print(f'unique\n{r.pop()+1}')
else:print(f'ambiguous\n{len(r)}')