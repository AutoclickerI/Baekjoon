N=int(input())
b=[[*map(int,input().split())]for _ in[0]*N]
input()
l=sorted(map(int,input().split()))
sl=[0]
while l:sl+=sl[-1]+l.pop(),

mv=0

prefix_sum_2d=[[0]*-~N]
prefix_sum_2d_cnt0=[[0]*-~N]
for i in b:
    tmp=[0]
    tmp_0=[0]
    for j in range(N):
        tmp+=tmp[-1]+prefix_sum_2d[-1][j+1]-prefix_sum_2d[-1][j]+i[j],
        tmp_0+=tmp_0[-1]+prefix_sum_2d_cnt0[-1][j+1]-prefix_sum_2d_cnt0[-1][j]+(i[j]==0),
    prefix_sum_2d+=tmp,
    prefix_sum_2d_cnt0+=tmp_0,

for y in range(N):
    for x in range(N):
        offset=1
        while max(x,y)+offset<=N:
            val=prefix_sum_2d[y+offset][x+offset]-prefix_sum_2d[y][x+offset]-prefix_sum_2d[y+offset][x]+prefix_sum_2d[y][x]
            cnt0=prefix_sum_2d_cnt0[y+offset][x+offset]-prefix_sum_2d_cnt0[y][x+offset]-prefix_sum_2d_cnt0[y+offset][x]+prefix_sum_2d_cnt0[y][x]
            if cnt0<len(sl):
                mv=max(mv,val+sl[cnt0])
            offset+=1
print(mv)