[n],*l=[[*map(int,i.split())]for i in open(0)]

A=sum(l[:n],[])

G=[[]for _ in[0]*-~n]
for a,b,c in l[n:]:
    G[a]+=(b,c),
    G[b]+=(a,c),

L=n.bit_length()
P=[[0]*-~n for _ in[0]*L]
D=[[0]*-~n for _ in[0]*L]

V=[0]*-~n
V[1]=1
S=[1]

while S:
    x=S.pop()
    for y,c in G[x]:
        if V[y]:
            continue
        V[y]=1
        P[0][y]=x
        D[0][y]=c
        S+=y,

for i in range(1,L):
    for j in range(1,n+1):
        P[i][j]=P[i-1][P[i-1][j]]
        D[i][j]=D[i-1][j]+D[i-1][P[i-1][j]]

for y,e in enumerate(A,1):
    for i in range(L-1,-1,-1):
        if P[i][y] and D[i][y]<=e:
            e-=D[i][y]
            y=P[i][y]
    print(y)