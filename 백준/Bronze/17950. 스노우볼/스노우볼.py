h,x,*l=map(int,open(0).read().split())
S=i=0
while i<h:S+=l[i]*pow(x,i:=i+1,R:=10**9+7)
print(S%R)