n,*l=map(int,open(0))
a=0
while l:p,q,*l=l;a+=p-q*3/5>8
print(a,end='+'*(n==a))