n,m,*l=map(int,open(i:=0).read().split())
while i<n*m:l[i]+=max(l[i-m]*(m<=i),l[i-1]*(0<i%m));i+=1
print(l[-1])