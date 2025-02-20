*l,t=map(int,open(0).read().split())
i=r=y=g=0
while t:k=min(t,l[i]);t-=k;i+=1;g+=k//i*(i<3);y+=(i in(3,5))*k;r+=(i>3)*k;i%=5
print(r,y,g)