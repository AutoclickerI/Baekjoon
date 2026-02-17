(xa1,ya1,xa2,ya2),(xb1,yb1,xb2,yb2)=sorted([*map(int,i.split())]for i in open(0))
if(xa2,ya2)==(xb1,yb1)or(xa2,ya1)==(xb1,yb2):
    print('POINT')
elif(ya2==yb1 or yb2==ya1)and xb1<xa2 or xa2==xb1 and(ya1<=yb1<=ya2 or yb1<=ya1<=yb2):
    print('LINE')
elif xa2<=xb1 or ya2<yb1 or yb2<ya1:
    print('NULL')
else:
    print('FACE')