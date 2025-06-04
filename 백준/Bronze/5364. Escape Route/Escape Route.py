_,[x,y],*l=[[*map(int,i.split())]for i in open(0)]
p,q=min(l,key=lambda i:(x-i[0])**2+(y-i[1])**2)
print(x,y,p,q,f'{abs(x-p+(y-q)*1j):.2f}')