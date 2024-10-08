while n:=int(input()):
    x1,y1,z1,r=zip(*eval('map(int, input().split()),'*n))
    x2=[i+j for i,j in zip(x1,r)]
    y2=[i+j for i,j in zip(y1,r)]
    z2=[i+j for i,j in zip(z1,r)]
    print(max(0,min(x2)-max(x1))*max(0,min(y2)-max(y1))*max(0,min(z2)-max(z1)))