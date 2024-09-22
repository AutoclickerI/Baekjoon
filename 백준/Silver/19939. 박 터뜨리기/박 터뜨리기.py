N,K=map(int,input().split())
N+=K*~K//2
print(-(N<0 or(N%K<1)-K))