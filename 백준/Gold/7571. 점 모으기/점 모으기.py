y,x=zip(*[map(int,i.split())for i in open(0)][1:])
y=sorted(y)
x=sorted(x)
my=sy=sum(y)
mx=sx=sum(x)
cy=cx=0
for i in range(len(y)):
    cy+=y[i]
    my=min(my,sy-cy-(len(y)-i-1)*y[i]+(i+1)*y[i]-cy)
for i in range(len(x)):
    cx+=x[i]
    mx=min(mx,sx-cx-(len(x)-i-1)*x[i]+(i+1)*x[i]-cx)
print(my+mx)