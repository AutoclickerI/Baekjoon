N,S=map(int,input().split())
N=N//4
R=input()
exec(S%3*'R=R[:N]+R[3*N:4*N]+R[N:3*N];')
print(R)