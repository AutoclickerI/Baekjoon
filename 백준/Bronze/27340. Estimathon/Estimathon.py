n,m,*l=map(int,open(c:=0).read().split())
for i in l:
    q=i//4
    if q==0:
        c=-1e9
    c+=q
print('NDEA'[m<=n<=c::2])