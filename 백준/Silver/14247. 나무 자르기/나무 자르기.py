[N],H,A=[sorted(map(int,i.split()))for i in open(0)]
print(sum(H)+sum(i*A[i]for i in range(N)))