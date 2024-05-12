*l,=map(int,[*open(0)][1].split())
a,b=sorted(l)[-2:]
print(*[x-[b,a][x==b]for x in l])