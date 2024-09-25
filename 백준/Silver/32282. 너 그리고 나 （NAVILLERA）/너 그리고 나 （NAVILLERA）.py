X,Y,c=map(int,input().split())
i=0
while(c*i)**2<X*X+Y*Y:i+=1
print(i+(0<X*X+Y*Y<c*c))