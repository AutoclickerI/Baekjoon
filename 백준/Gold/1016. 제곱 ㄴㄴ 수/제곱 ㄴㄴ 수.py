m,M=map(int,input().split())
*l,=range(m,M+1)
for i in range(2,2*10**6):
    n=i*i
    s=m//n*n
    if s==m:l[0]=0
    while(s:=s+n)<=M:
        l[s-m]=0
print(M-m+1-l.count(0))