[N],*b=[[*map(int,i.split())]for i in open(0)]
N=int(N)
I=[[i==j for j in range(N)]for i in range(N)]
for i,j in zip(b,I):
    i+=j

for i in range(N):
    for j in range(i,min(i+3,N)):
        if 1e-8<abs(b[j][i]):
            break
    else:
        exit(print(-1))
    b[i],b[j]=b[j],b[i]
    for j in range(i+1,min(i+2,N)):
        if b[j][i]:
            div=b[j][i]/b[i][i]
            for k in range(2*N):
                b[j][k]-=div*b[i][k]*(2*(k<N)-1)

for i in range(N):
    if abs(b[i][i+N])<1e-8:
        exit(print(-1))
for i in b:
    print(*[f'{v:.3f}'for v in i[N:]])

for i in b:
    print(*[f'{v:.3f}'for v in i[:N]])