A,[*B]=zip(*[map(int,i.split())for i in open(0)])
for i in range(100):x=i%3;y=-~i%3;z=min(A[y]-B[y],B[x]);B[y]+=z;B[x]-=z
print(*B)