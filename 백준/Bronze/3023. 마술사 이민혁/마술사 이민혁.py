_,*l,k=open(0)
l=[[*i[:-1]+i[-2::-1]]for i in l+l[::-1]]
A,B=map(int,k.split())
l[A-1][B-1]='.#'['#'<l[A-1][B-1]]
for i in l:print(*i,sep='')