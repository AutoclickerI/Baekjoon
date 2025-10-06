N,M,S,R=map(int,input().split())

if M<N-1 or (N-1)*N//2<M or S<N-1 or (N-1)*R<S:
    print(-1)
else:
    m=S//(N-1)
    t=S%(N-1)
    for i in range(N):
        for j in range(i+1,N):
            if M:
                print(i+1,j+1,[m,m+1][N-t-1<j])
                M-=1
            else:
                break