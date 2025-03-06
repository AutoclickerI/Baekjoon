N,M,A,B=map(int,input().split())
p=N//M
print(N+min(N*B,p*A+N%M*B,-~p*A))