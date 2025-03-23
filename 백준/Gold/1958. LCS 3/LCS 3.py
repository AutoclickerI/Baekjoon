A=input()
B=input()
C=input()

v=[[[0]*-~len(A)for _ in[0]*-~len(B)]for _ in[0]*-~len(C)]

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            v[k+1][j+1][i+1]=max(v[k][j+1][i+1],v[k+1][j][i+1],v[k+1][j+1][i],v[k][j][i]+(A[i]==B[j]==C[k]))

print(v[-1][-1][-1])
