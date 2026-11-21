N,M,A,B=map(int,input().split())
M-=3*N
print((M<0)*(B-A*M))