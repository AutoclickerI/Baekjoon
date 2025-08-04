N,K,*l=map(int,open(0).read().split())
for i in range(N*N):
 j=i%N
 if~j>i//N-N<0<l[j+1]<l[j]:K-=1;l[j:j+2]=l[j+1],l[j];K<1<exit(print(*l))
print(-1)