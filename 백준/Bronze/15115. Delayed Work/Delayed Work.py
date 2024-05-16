K,P,X=map(int,input().split())
t=K*P/X
M=int(t**.5)
print(f'{X*min(M+t/M,t/-~M-~M):.3f}')