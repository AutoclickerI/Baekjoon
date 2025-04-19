b=[input()for _ in[0]*5]
f=0
c=0
for y in range(5):
    for x in range(5):
        c+=b[y][x]=='k'
        for dy,dx in(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2):
            if 0<=y+dy<5>x+dx>=0:f|=b[y][x]=='k'==b[y+dy][x+dx]
print((f or c!=9)*'in'+'valid')