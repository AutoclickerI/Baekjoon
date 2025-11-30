_,A,*z=[[*map(int,i.split())]for i in open(0)]
for l,h in z:A[l-1]-=A[h-1]!=max(A)
print(*A)