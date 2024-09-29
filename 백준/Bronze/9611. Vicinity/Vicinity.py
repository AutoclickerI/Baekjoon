f=lambda:[*map(int,input().split())]
p=eval('f(),'*f()[0])
exec('i,d=f();x,y=p[i-1];print(sum((x-a)**2+(y-b)**2<=d*d for a,b in p)-1);'*f()[0])