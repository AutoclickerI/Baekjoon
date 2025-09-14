X,Y,N=map(int,open(0).read().split())
f=lambda n:(10**~-n-1//n,10**n-1)
l,r=f(X)
L,R=f(Y)
c=min(r,N-L)-max(l,N-R)+1
print(c-c//2*(X==Y))