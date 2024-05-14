a,b,c,x,y=map(int,input().split())
d=min(x,y)
print(min(k:=a*x+b*y,k-(a+b)*d+c*d*2,c*max(x,y)*2))