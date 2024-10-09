g=eval('10*[1],'*10)
for _ in[0]*int(input()):
    for i in g:
        for j in range(10):i[j]+=1
    *c,=map(int,input().split())
    for a in c[:3]:
        for i in range(10):
            g[a-1][i]=1
    for a in c[3:]:
        for i in range(10):
            g[i][a-1]=1
for i in g:print(*i)