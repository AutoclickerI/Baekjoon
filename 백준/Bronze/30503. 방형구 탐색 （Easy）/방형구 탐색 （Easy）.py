N=int(input())
*A,=map(int,input().split())
for _ in[0]*int(input()):
    n,*l=map(int,input().split())
    if n-1:
        l,r=l
        A[l-1:r]=[0]*(r-l+1)
    else:
        l,r,k=l
        print(A[l-1:r].count(k))