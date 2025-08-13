N,M,*l=map(int,open(0).read().split())
print(*min([(i//M+abs(M//2-i%M),i//M+1,i%M+1)for i in range(N*M)if l[i]<1]or[[-1]*2])[1:])