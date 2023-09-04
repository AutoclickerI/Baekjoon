n,t=map(int,input().split())
t%=4*n-2
print(2*n-abs(t-2*n)or 2)