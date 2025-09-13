n,d,k=map(int,input().split())
r=[(0,0)]
i=y=x=0
j=h=1
while 0<n:exec("r+=[(x:=x+i,y:=y+j)]*(0<n);n-=1;"*d);i,j=j,-i;h^=1;d*=h*~-k+1
(p,*_,q),(u,*_,v)=map(sorted,zip(*r))
print(q-p+1,v-u+1,*[''.join('.*'[(x,y)in r]for y in range(u,v+1))for x in range(q,p-1,-1)])