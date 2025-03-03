N,M=map(int,input().split())
U,V=map(int,input().split())

tile=[input()for _ in[0]*U]
s=input()[0]

if s=='c':
    for i in range(U):
        tile[i]=tile[i]+tile[i][-1]*200
    tile+=[tile[-1]]*200
elif s=='r':
    for i in range(U):
        tile[i]=tile[i]*200
    tile*=200
else:
    for i in range(U):
        tile[i]=(tile[i]+tile[i][::-1])*100
    tile+=tile[::-1]
    tile*=100

for i in range(N):
    print(tile[i][:M])