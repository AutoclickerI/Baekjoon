A,B=input().split()
for c in A:
    if c in B:break
N=len(A)
M=len(B)
ia=A.find(c)
ib=B.find(c)
for i in range(ib):
    print('.'*ia+B[i]+'.'*(N+~ia))
print(A)
for i in range(ib+1,M):
    print('.'*ia+B[i]+'.'*(N+~ia))