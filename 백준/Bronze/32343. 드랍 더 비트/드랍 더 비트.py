N,a,b=map(int,open(0).read().split())
x=min(a+b,2*N-a-b)
print(2**x-1<<N-x)