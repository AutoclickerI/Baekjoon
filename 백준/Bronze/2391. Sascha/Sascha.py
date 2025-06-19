_,*l=open(0)
while l:s,n,*l=l;n=int(n);print(end=min(l[:n],key=lambda i:sum(map(str.__ne__,s,i))));l=l[n:]