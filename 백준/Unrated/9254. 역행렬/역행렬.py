[N],*b=[[*map(int,i.split())]for i in open(0)]
N=int(N)
I=[[i==j for j in range(N)]for i in range(N)]
for i,j in zip(b,I):
    i+=j

for i in range(N):
    for j in range(i,N):
        if 1e-8<abs(b[j][i]):
            break
    else:
        exit(print('no inverse'))
    b[i],b[j]=b[j],b[i]
    div=b[i][i]
    for j in range(2*N):
        b[i][j]/=div
    for j in range(i+1,N):
        if b[j][i]:
            div=b[j][i]
            for k in range(2*N):
                b[j][k]-=div*b[i][k]
for i in range(N)[::-1]:
    for j in range(i):
        if b[j][i]:
            div=b[j][i]
            for k in range(2*N):
                b[j][k]-=div*b[i][k]
for i in b:
    print(*[f'{v:.10f}'for v in i[N:]])