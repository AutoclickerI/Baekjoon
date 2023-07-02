p,q,r=map(int,input().split())
s=(p+q+r)/2
a,b,c=s-r,s-q,s-p
if a>0<b>0<c:print(1,a,b,c)
else:print(-1)