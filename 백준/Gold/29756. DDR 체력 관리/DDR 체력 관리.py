N,K=map(int,input().split())
l=[101*[0]for _ in[0]*-~N]
for i,j in zip(map(int,input().split()),map(int,input().split())):
    tmp=[0]*K+l[-1]
    tmp=tmp[:100]+[max(tmp[100:])]
    for k in range(j,101):
        tmp[min(100,k-j+K)]=max(tmp[min(100,k-j+K)],l[-1][k]+i)
    l+=tmp,
print(max(l[-1]))