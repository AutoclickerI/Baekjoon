N,U,D=map(int,input().split())
*A,=map(int,input().split())
*B,=map(int,input().split())

delta=[0]*-~N
ds=[0]*-~N
s=0
acc=0
for i in range(N):
    acc-=delta[i]
    s+=ds[i]
    if B[i]<=A[i]:
        s+=B[i]+acc
        acc-=D
    else:
        d=0-(A[i]-B[i])//(U+D)
        delta[min(N,i+d)]+=U+D
        ds[min(N,i+d)]+=B[i]-A[i]-(U+D)*(d-1)
        s+=A[i]+acc
        acc+=U
    print(s)