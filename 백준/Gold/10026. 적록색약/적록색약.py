n,*m=open(0)
n=int(n)
m=''.join(m)+' '*n
for l in[*m],[ord(i)//14for i in m]:
 i=t=0
 while i<n*n:
  if c:=l[q:=i+i//n]:q=[q];t+=1;[exec((l[x]==c)*"l[x]=0;q+=x+1,x-1,x+~n,x-~n")for x in q]
  i+=1
 print(t)