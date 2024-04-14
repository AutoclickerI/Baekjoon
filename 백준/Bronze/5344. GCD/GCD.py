for i in[*open(0)][1:]:
 n,m=map(int,i.split())
 while m:n,m=m,n%m
 print(n)