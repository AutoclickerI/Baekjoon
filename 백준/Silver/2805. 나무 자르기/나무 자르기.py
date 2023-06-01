_,n,*l=map(int,open(0).read().split())
t=[0,max(l)]
while t[1]-t[0]-1:m=sum(t)//2;t[sum(max(0,i-m)for i in l)<n]=m
print(t[0])