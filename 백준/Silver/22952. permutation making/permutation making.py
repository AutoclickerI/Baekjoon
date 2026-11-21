N=int(input())
l,r,*x=1,N-1
while l<r:x+=l,r;l+=1;r-=1
print(*x+(l==r)*[l],N)