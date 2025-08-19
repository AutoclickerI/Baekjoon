n,*l=map(int,open(0).read().split())
i=v=1
while i<n:v&=l[i];i=i*2+1
print('YNeos'[v*-~i<2*n::2])