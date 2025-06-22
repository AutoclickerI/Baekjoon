n,i,k=map(int,input().split())
print(((~-i/n)**k*i-~n-sum((j/n)**k for j in range(i-1,n)))/2)