[R,C],*b,[T]=[[*map(int,i.split())]for i in open(0)]
r=0
for y in range(R-2):
    for x in range(C-2):
        r+=T<=sorted(b[y+i][x+j]for i in(0,1,2)for j in(0,1,2))[4]
print(r)