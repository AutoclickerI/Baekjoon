n,T,m,x,y=map(int,open(0).read().split())
print(int(max(-(((n-m)/y+m/x)/60//-1)-T,0)))