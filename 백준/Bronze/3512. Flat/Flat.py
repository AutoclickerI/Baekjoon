N,M=map(int,input().split())
r=B=b=0
for i in[0]*N:
    p,q=input().split()
    p=int(p)
    if q=='balcony':b+=p
    elif q=='bedroom':B+=p
    else:r+=p
print(r+B+b)
print(B)
print(M*(r+B+b*.5))