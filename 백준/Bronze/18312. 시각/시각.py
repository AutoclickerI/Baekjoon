H=M=S=A=0
N,K=input().split()
while H<=int(N):
    A+=K in f'{H:02d}{M:02d}{S:02d}'
    H+=M==59==S
    M=(M+(S==59))%60
    S=(S+1)%60
print(A)