W,H,x,y,p,q,r,_=map(int,open(0).read().split())
a,b=[min(max(x+(i-x)/(y-q)*y,0),W)for i in[p,r]]
print(max(b-a,0)/W)