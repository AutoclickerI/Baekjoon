N,M=map(int,input().split())
b1=[input()for _ in[0]*N]
b2=[input()for _ in[0]*N]

b=[[k!=l for k,l in zip(i,j)]for i,j in zip(b1,b2)]

c=0

for y in range(N-2):
    for x in range(M-2):
        if b[y][x]:
            for dy in range(3):
                for dx in range(3):
                    b[y+dy][x+dx]^=1
            c+=1

if max(max(b)):print(-1)
else:print(c)