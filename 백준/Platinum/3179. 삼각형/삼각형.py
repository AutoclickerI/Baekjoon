n=int(input())
point=[[*map(int,input().split())]for _ in[0]*n]
ccw=lambda *l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(3))
ccwdata=[[0 for _ in[0]*n]for _ in[0]*n]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j:
                tmp=ccw(point[i],point[j],point[k])<=0
                ccwdata[i][j]+=tmp
maxval=-1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tmp=ccw(point[i],point[j],point[k])
            if tmp==0:
                continue
            elif tmp<0:
                tmp1=ccwdata[i][j]
                tmp2=ccwdata[j][k]
                tmp3=ccwdata[k][i]
            else:
                tmp1=ccwdata[i][k]
                tmp2=ccwdata[k][j]
                tmp3=ccwdata[j][i]
            val=tmp1+tmp2+tmp3-2*n
            if val>maxval:
                ans=i,j,k
                maxval=val
print(maxval)
print(*(i+1 for i in ans))