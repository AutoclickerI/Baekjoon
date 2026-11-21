a,b,c,x,y=map(int,input().split())
print(min(k:=a*x+b*y,k-(a+b-2*c)*min(x,y),c*max(x,y)*2))