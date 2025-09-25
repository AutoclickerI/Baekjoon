(_,t),*l=[[*map(int,i.split())]for i in open(0)]
z=l[0]
l.sort()
print(sorted(x+v*t for x,v in l)[l.index(z)])