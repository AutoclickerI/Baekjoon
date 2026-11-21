m=[[*map(int,i.split())]for i in open(0)][1:]
while any(map(lambda a:any(i>j for i,j in zip(a,a[1:])),m+[*zip(*m)])):m=[*zip(*m)][::-1]
for i in m:print(*i)