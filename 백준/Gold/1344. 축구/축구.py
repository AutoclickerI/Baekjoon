p1,p2=map(int,open(0))
p1/=100
p2/=100

def poly_mul(A,B):
    v=[0]*(len(A)+len(B)-1)
    for i in range(len(A)):
        for j in range(len(B)):
            v[i+j]+=A[i]*B[j]
    return v

def poly_pow(A,k):
    if k==1:
        return A
    r=poly_pow(A,k//2)
    r=poly_mul(r,r)
    if k%2:
        r=poly_mul(A,r)
    return r

p1=[1-p1,p1]
p2=[1-p2,p2]

p1=poly_pow(p1,18)
p2=poly_pow(p2,18)

p=[2,3,5,7,11,13,17]

p1=sum(p1[i]for i in p)
p2=sum(p2[i]for i in p)

print(1-(1-p1)*(1-p2))