_,*l,k=open(0)
l=[i[:-1]+i[-2::-1]for i in l]
l+=l[::-1]
A,B=map(int,k.split())
*v,=l[A-1]
v[B-1]='.#'['#'<v[B-1]]
l[A-1]=''.join(v)
for i in l:print(i)