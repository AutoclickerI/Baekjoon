n=int(input())
point=[[*map(int,input().split())]for _ in[0]*n]
ccw=lambda *l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(3))
ccwdata=[[[0]*n for _ in[0]*n]for _ in[0]*n]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j!=k!=i:ccwdata[i][j][k]=ccw(point[i],point[j],point[k])
ccwdata2=[[sum(j<=0 for j in k)for k in i]for i in ccwdata]
maxval=-10**18
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tmp=ccw(point[i],point[j],point[k])
            if tmp==0:
                continue
            elif tmp<0:
                tmp1=ccwdata2[i][j]
                tmp2=ccwdata2[j][k]
                tmp3=ccwdata2[k][i]
            else:
                tmp1=ccwdata2[i][k]
                tmp2=ccwdata2[k][j]
                tmp3=ccwdata2[j][i]
            val=tmp1+tmp2+tmp3
            if val>maxval:
                ans=i,j,k
                maxval=val
i,j,k=ans
if ccwdata[i][j][k]<0:
    tmp1=ccwdata[i][j]
    tmp2=ccwdata[j][k]
    tmp3=ccwdata[k][i]
else:
    tmp1=ccwdata[i][k]
    tmp2=ccwdata[k][j]
    tmp3=ccwdata[j][i]
val=0
for order in range(n):
    if tmp1[order]<=0 and tmp2[order]<=0 and tmp3[order]<=0:
        val+=1
print(val)
print(*(i+1 for i in ans))