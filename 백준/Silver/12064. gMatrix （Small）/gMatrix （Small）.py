I=lambda:[*map(int,input().split())]

for i in range(*I()):
    N,K,C,X=I()
    A,B=I(),I()
    M=[[(C-A[i]*~i-B[j]*~j)%X for j in range(N)]for i in range(N)]
    print(f'Case #{i+1}: {sum(max(M[p][q] for p in range(i,i+K)for q in range(j,j+K))for i in range(N-K+1)for j in range(N-K+1))}')