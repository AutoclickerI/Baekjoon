N,M=map(int,input().split())
R=range(1,10)
print(sum(M>=N-10**i//9*j>-1for i in R for j in R))