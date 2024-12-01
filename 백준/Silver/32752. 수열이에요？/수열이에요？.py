N,L,R=map(int,input().split())
*A,=map(int,input().split())
A2=sorted(A)
c=''.join(str(+(i!=j))for i,j in zip(A,A2))
i1=c.find('1')
i2=c.rfind('1')

if i1<0 or L-2<i1<=i2<R:
    print(1)
else:
    print(0)