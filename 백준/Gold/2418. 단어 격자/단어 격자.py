H,W,L=map(int,input().split())
b=[input()for _ in[0]*H]
s=input()
l=[[i==s[0]for i in j]for j in b]
for i in s[1:]:
    tmp=[W*[0]for _ in[0]*H]
    for x in range(H):
        for y in range(W):
            for dx in-1,0,1:
                for dy in-1,0,1:
                    if dx==dy==0 or x+dx<0 or y+dy<0 or H<=x+dx or W<=y+dy:continue
                    tmp[x][y]+=l[x+dx][y+dy]*(b[x][y]==i)
    l=tmp
print(sum(sum(l,[])))