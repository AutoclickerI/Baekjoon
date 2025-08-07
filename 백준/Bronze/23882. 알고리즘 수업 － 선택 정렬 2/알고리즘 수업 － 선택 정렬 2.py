N,K=map(int,input().split())
*A,=map(int,input().split())

for i in range(N)[::-1]:
    v=A.index(max(A[:i+1]))
    if i!=v:
        K-=1
        A[i],A[v]=A[v],A[i]
        K<1<exit(print(*A))
    
print(-1)