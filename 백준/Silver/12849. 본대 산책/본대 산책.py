N=int(input())

# 정보과학, 전산, 미래, 신양, 한경, 진리, 학생, 형남

l=[[1,0,0,0,0,0,0,0]]

mat=[[0,1,1,0,0,0,0,0],
     [1,0,1,1,0,0,0,0],
     [1,1,0,1,1,0,0,0],
     [0,1,1,0,1,1,0,0],
     [0,0,1,1,0,1,0,1],
     [0,0,0,1,1,0,1,0],
     [0,0,0,0,0,1,0,1],
     [0,0,0,0,1,0,1,0]]

def matmul(a,b):
    return[[sum(i*j for i,j in zip(r,c))%1000000007 for c in zip(*b)]for r in a]

def matpow(a,k):
    if k==1:
        return a
    t=matpow(a,k//2)
    if k%2:
        return matmul(a,matmul(t,t))
    else:
        return matmul(t,t)

print(matmul(l,matpow(mat,N))[0][0])