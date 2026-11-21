n,m,*a=map(int,open(0).read().split())
z=i=0
while-~i<n:f=abs(a[i]-a[i:=i+1])<m;a[f*i]=-m;z+=f
print(z)