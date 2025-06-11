[N,M],*l=[[*map(int,i.split())]for i in open(0)]
print(max((x-p)**2+(y-q)**2for x,y in l[:N]for p,q in l[N:]))