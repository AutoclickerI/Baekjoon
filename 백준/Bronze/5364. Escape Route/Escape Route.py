n,[x,y],*l=[[*map(int,i.split())]for i in open(0)]
f=lambda a:abs(a[0]-x+(a[1]-y)*1j)
m=min(l,key=f)
print(x,y,*m,'%.2f'%f(m))