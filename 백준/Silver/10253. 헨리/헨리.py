for i in[*open(0)][1:]:
 n,m=map(int,i.split())
 while n:t=-m//n;n=t*n+m;m*=t
 print(-t)