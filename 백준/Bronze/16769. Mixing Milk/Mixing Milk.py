A,[*B]=zip(*[map(int,i.split())for i in open(0)])
for i in range(100):z=min(A[y:=-~i%3]-B[y],B[i%3]);B[y]+=z;B[i%3]-=z
print(*B)