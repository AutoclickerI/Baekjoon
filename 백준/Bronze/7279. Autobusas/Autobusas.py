N,K=map(int,input().split())
s=m=0
for _ in[0]*N:
    s+=eval(input().replace(*' -'))
    m=max(m,s-K)
print(m)