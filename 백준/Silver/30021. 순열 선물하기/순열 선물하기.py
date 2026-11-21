n=int(input())
f=n!=2
print('NYOE S'[f::2],*(1,3,2,*range(4,n+1))[:n*f])