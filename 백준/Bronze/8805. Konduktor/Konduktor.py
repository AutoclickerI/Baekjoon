for i in[*open(0)][1:]:
 n,k=map(int,i.split());r=[k];n-=1
 if n:x,y=divmod(k-1,n*2);r=x+1,*[2*x+(i<y)+(n*2-2-i<y)>>(i==n-1)for i in range(n)]
 print(*r)