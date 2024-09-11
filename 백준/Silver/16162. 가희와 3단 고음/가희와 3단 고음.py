N,A,D,*l=map(int,open(a:=0).read().split())
for i in l:f=i==A;A+=D*f;a+=f
print(a)