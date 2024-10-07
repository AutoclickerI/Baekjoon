from fractions import*
n,p,q=map(int,input().split())
print(*sorted({Fraction(i,j)for i in range(n+1)for j in range(1,n+1)if q<p*q*i/j<p}))