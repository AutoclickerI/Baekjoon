n,*l=open(0)
N,S,E,T=map(int,n.split())
V=N*5

M=[V*[0]for _ in[0]*V]

for i in range(N):
    for j,c in enumerate(l[i][:-1]):
        w=int(c)
        if w:
            M[i*5][j*5+w-1]=1

    for j in range(1,5):
        M[i*5+j][i*5+j-1]=1

def matmul(a,b):
    return[[sum(i*j for i,j in zip(r,c))%1000003 for c in zip(*b)]for r in a]

R=[V*[0]for _ in[0]*V]

for i in range(V):
    R[i][i]=1

while T:
    if T&1:
        R=matmul(R,M)
    
    M=matmul(M,M)
    T//=2

print(R[(S-1)*5][(E-1)*5])