_,[x,y],*l=[[*map(int,i.split())]for i in open(0)]
p,q=min(l,key=lambda i:(x-i[0])**2+(y-i[1])**2)
print(x,y,p,q,f'{((x-p)**2+(y-q)**2)**.5:.2f}')