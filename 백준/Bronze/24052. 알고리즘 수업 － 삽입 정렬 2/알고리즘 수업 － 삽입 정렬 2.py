N,K=map(int,input().split())
*A,=map(int,input().split())

def modify(p,v):
    global K
    K-=1
    A[p]=v
    K<1<exit(print(*A))

for i in range(1,N):
    loc=i-1
    n=A[i]
    while 0<=loc and n<A[loc]:
        modify(loc+1,A[loc])
        loc-=1
    if loc+1!=i:
        modify(loc+1,n)

print(-1)