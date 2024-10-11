a=eval('[*map(int,input().split())],'*3)
for i in range(3):
    for j in range(3):
        if a[i][j]<9:
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):a[i][j]+=3>x>-1<y<3<8<a[x][y]
for r in a:print(*r)