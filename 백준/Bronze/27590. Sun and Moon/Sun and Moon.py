p,q,r,s=map(int,open(0).read().split())
i=0
while(p+i)%q-(r+i)%s:i+=1
print(i)