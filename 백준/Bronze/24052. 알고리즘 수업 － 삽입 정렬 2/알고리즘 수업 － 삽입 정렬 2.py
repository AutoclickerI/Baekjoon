N,K,*A=map(int,open(0).read().split())

def f(v):
    global K
    K-=1
    A[p+1]=v
    K<1<exit(print(*A))

for i in range(1,N):
    p=i-1
    n=A[i]
    while 0<=p and n<A[p]:
        f(A[p])
        p-=1
    if p+1!=i:
        f(n)

print(-1)