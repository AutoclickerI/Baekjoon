h1,d1,t1,h2,d2,t2=map(int,open(0).read().split())
t=0
while h1>0<h2:h2-=d1*(t%t1==0);h1-=d2*(t%t2==0);t+=1
if h1<1:
    if h2<1:print('draw')
    else:print('player two')
else:
    print('player one')