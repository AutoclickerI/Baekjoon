while n:=int(input()):
    x,y,z,r=zip(*eval('map(int,input().split()),'*n))
    X,Y,Z=[[i+j for i,j in zip(k,r)]for k in[x,y,z]]
    print(max(0,min(X)-max(x))*max(0,min(Y)-max(y))*max(0,min(Z)-max(z)))