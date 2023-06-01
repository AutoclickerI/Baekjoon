N,K=map(int,input().split())
*X,=map(int,input())
k=0
while K:X=K%2*[X[(j+2**k)%N]^X[j-2**k%N]for j in range(N)]or X;K//=2;k+=1
print(*X,sep='')