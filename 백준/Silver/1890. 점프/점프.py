N=int(input())
b=[[*map(int,input()[::2])]for _ in[0]*N]

v=[N*[0]for _ in[0]*N]
v[0][0]=1
for y in range(N):
    for x in range(N):
        if x+b[y][x]<N:v[y][x+b[y][x]]+=v[y][x]
        if y+b[y][x]<N:v[y+b[y][x]][x]+=v[y][x]
print(v[-1][-1]//4)