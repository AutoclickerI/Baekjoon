N,M,*l=map(int,open(0).read().split())
print(max(sum(max(l[j+k*M]for j in[i%M,i//M%M,i//M**2])for k in range(N))for i in range(M**3)))