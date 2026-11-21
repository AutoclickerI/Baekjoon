*_,x,y=sorted(l:=[*map(int,[*open(0)][1].split())])
print(*[z-[x,y][z<y]for z in l])