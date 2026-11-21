N,K=map(int,input().split())
*A,=map(int,input().split())
*B,=map(int,input().split())
sA=sum(A)
sB=sum(B)
for _ in[0]*K:
    if sA<sB:
        sB-=B.pop()
    else:
        sA-=A.pop()
print(max(sA,sB))