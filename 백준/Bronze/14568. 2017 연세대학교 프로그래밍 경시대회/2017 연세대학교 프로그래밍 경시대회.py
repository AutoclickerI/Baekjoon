n=int(input())
R=range(100)
print(sum(i*j*k and i-j>1and(k+1)%2and i+j+k==n for i in R for j in R for k in R))