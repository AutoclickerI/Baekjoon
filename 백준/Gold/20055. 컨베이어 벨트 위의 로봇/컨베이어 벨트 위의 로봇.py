N,K,*A=map(int,open(0).read().split())

r=[0]*N

A_i=0

while A.count(0)<K:
    A_i-=1
    r=[0]+r[:-2]+[0]
    for i in range(N-1)[::-1]:
        if(r[i],r[i+1])==(1,0)and A[(A_i+i+1)%(2*N)]:
            A[(A_i+i+1)%(2*N)]-=1
            r[i]=0
            r[i+1]=1
    if A[A_i%(2*N)]:
        r[0]=1
        A[A_i%(2*N)]-=1
    r[-1]=0

print(-A_i)