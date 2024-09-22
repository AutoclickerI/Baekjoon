*a,=map(int,open(0).read().split())
x,y,z=[min(a[i+3::6])-max(a[i::6])for i in[1,2,3]]
print(x*y*z*(min(x,y,z)>0))