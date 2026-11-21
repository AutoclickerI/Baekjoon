def f(l):t=l[0];return-~sum(t<(t:=max(i,t))for i in l)
l=[[*map(int,i.split())]for i in open(0)][1:]
print(*map(f,[*zip(*l)]+l))