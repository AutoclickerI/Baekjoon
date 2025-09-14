P,D,N=map(eval,input().split())
y=v=f=0
while(P-D)*12>f:f=int(v*N-D*1200+D*N/((1+N/100)**(1/12)-1)+.5)/100;y+=1;v+=D*12+f
print(y)