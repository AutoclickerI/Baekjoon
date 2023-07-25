n,k,d,s=map(int,open(0).read().split())
x=(n*d-k*s)/(n-k)
print(x*(0<=x<=100)or'impossible')