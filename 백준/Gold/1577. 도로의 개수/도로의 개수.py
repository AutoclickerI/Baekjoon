[N,M],_,*l=[[*map(int,i.split())]for i in open(0)]

p=[-~M*[-1]for _ in[0]*-~N]
p[0][0]=1
s=set()
for a,b,c,d in l:
    (a,b),(c,d)=sorted(((a,b),(c,d)))
    s.add((a,b,c,d))

for i in range(1,N+M+1):
    for j in range(i+1):
        if j<=N and i-j<=M:
            p[j][i-j]=(p[j-1][i-j]if 0<j and (j-1,i-j,j,i-j)not in s else 0)+(p[j][i-j-1]if 0<i-j and (j,i-j-1,j,i-j)not in s else 0)
print(p[N][M])