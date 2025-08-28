def matmul(A,B):
    return[[+any(i*j for i,j in zip(k,l))for l in zip(*B)]for k in A]

l=[[i=='Y'for i in j[:-1]]for j in[*open(0)][1:]]

for i in range(len(l)):l[i][i]=1

nl=matmul(l,l)

for i in range(len(l)):nl[i][i]=0

print(max(sum(i)for i in nl))