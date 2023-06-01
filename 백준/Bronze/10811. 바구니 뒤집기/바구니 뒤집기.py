N,M,*l=map(int,open(0).read().split())
*L,=range(N+1)
while l:i,j,*l=l;L[i:j+1]=L[j:i-1:-1]
print(*L[1:])