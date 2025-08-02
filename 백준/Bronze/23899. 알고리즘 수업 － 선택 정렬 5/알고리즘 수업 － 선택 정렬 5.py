[N],A,B=[[*map(int,i.split())]for i in open(0)]

f=0
for i in range(1,N)[::-1]:
    f|=A==B
    k=A.index(max(A[:i+1]))
    A[k],A[i]=A[i],A[k]
print(f|(A==B))