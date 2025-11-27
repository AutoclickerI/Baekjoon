[N,M],*l=[map(int,i.split())for i in open(0)]
b=[{0}for _ in[0]*-~N]
t=N*~-N*(N-2)//6
for x,y in l:t-=N+~len(b[x]|b[y]);b[x]|={y};b[y]|={x}
print(t)