n,*a=map(int,open(0).read().split())
x,y,z=sorted(map(min,a,a[:2:-1]))
print(((5*n*n-8*n+4)*x+8*~-n*y+4*z,sum(a)-max(a))[n<2])