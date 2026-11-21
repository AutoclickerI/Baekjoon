N,M=map(int,input().split())
l=[0,*map(int,input().split())]
for _ in[0]*M:
    a,b,c=map(int,input().split())
    if a<2:
        l[b]=c
    elif a<3:
        for i in range(b,c+1):l[i]^=1
    elif a<4:
        for i in range(b,c+1):l[i]=0
    else:
        for i in range(b,c+1):l[i]=1
print(*l[1:])
        