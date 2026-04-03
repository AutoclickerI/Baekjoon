[N],H,A=[sorted(map(int,i.split()))for i in open(0)]
print(sum(H+[i*A[i]for i in range(N)]))