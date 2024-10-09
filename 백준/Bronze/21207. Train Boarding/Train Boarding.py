n,l,p,*a=map(int,open(0).read().split())
c=[m:=0]*n*l
for x in a:c[y:=min(x//l*l,n*l-l)+l//2]+=1;m=max(m,abs(y-x))
print(m,max(c))