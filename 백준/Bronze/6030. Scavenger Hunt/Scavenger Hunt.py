p,q=map(int,input().split())
for n in[i for i in range(1,p+1)if p%i==0]:
    for m in[i for i in range(1,q+1)if q%i==0]:print(n,m)