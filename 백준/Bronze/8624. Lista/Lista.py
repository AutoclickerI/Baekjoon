n,k,i,j=map(int,input().split())
print((2*k-2*n-i-j)*(i+~j)//2-n*(j>k)*(j-max(i-1,k)))