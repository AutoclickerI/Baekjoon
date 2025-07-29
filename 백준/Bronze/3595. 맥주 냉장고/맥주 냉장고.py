n=int(input())
print(*min(min(((i*j+n//j+n//i),i,j,n//i//j)for j in range(1,int((n//i)**.5)+1)if n//i%j<1)for i in range(1,int(n**.5)+1)if n%i<1)[1:])