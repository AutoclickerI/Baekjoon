n,r,x,*l=map(int,open(0).read().split())
t=c=0
for i in l:v=min(c:=min(c+i,r),x);t+=v;c-=v
print(t)