j=''.join
f=lambda:[int(j(l[i:i+2]))for l in[[str(int(j(i),2))for i in zip(*eval('input().split(),'*4))]]for i in range(0,6,2)]
a,b,c=map(sum,zip(f(),f()))
t=a*3600+b*60+c
for i in zip(*map(lambda i:f'000{int(i):b}'[-4:],'%02d%02d%02d'%(t//3600%24,t//60%60,t%60))):print(*i)