N,M=map(int,input().split())
b=[input()for _ in[0]*N]

m=0
for i in range(min(N,M)):
    for y in range(N-i):
        for x in range(M-i):
            if b[y][x]==b[y][x+i]==b[y+i][x]==b[y+i][x+i]:
                m=~i
print(m*m)