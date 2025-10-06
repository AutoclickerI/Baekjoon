N,M=map(int,input().split())
b=[input()for _ in[0]*N]

arr=[[0]*-~M]
for i in range(N):
    tmp=[0]
    for c in range(M):
        if b[i][c]<'1':
            tmp+=0,
        else:
            mv=min(tmp[-1],arr[-1][c+1])
            tmp+=mv+(b[i-mv][c-mv]=='1'),
    arr+=tmp,
print(max(sum(arr,[]))**2)