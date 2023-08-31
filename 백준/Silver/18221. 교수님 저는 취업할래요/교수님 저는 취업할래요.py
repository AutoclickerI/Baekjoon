n=int(input())
l=[input().split()for _ in[0]*n]
for i in range(n):
    for j in range(n):
        if l[i][j]=='5':prof=i,j
        if l[i][j]=='2':sg=i,j
a,b=min(prof[0],sg[0]),max(prof[0],sg[0])
c,d=min(prof[1],sg[1]),max(prof[1],sg[1])
if(a-b)**2+(c-d)**2<25:
    print(0)
else:
    cnt=0
    for i in range(a,b+1):
        for j in range(c,d+1):
            cnt+=l[i][j]=='1'
    print(+(cnt>2))