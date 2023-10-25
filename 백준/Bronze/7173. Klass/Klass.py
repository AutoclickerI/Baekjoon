N,M=map(int,input().split())
l=[input()for _ in[0]*N]
ans=0
for i in range(N):
    for j in range(M):
        cnt=0
        val=0
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            if 0<=i+dy<N and 0<=j+dx<M:
                cnt+=1
                val+=abs(int(l[i][j])-int(l[i+dy][j+dx]))
        ans+=val/cnt
print(f'{ans:.4f}')