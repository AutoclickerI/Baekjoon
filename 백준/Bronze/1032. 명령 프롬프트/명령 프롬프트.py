def b(A):return [[A[i][j]for i in range(len(A))]for j in range(len(A[0]))]
a=b([list(input())for i in range(int(input()))])
for i in range(len(a)):a[i].sort()
[print(a[i][0]if a[i][0]==a[i][-1]else'?', end='')for i in range(len(a))]