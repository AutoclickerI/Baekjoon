N,*l=map(int,open(0).read().split())
v=[N]*-~N
for i in l:v[i]=v[i-1]-1
print(min(v))