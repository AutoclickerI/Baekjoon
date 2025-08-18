(n,m),*l,(C11,C12,C21,C22)=[[*map(int,i.split())]for i in open(0)]
B=[m*[0]for _ in range(n)]
for i in range(n):
    for j in range(m):
        v=l[i][j]
        if 0<i and 0<j:v-=B[i-1][j-1]*C11
        if 0<i:v-=B[i-1][j]*C12
        if 0<j:v-=B[i][j-1]*C21
        B[i][j]=v//C22
for i in B:print(*i)