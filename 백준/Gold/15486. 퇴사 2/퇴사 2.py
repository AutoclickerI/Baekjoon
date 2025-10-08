n=int(input())
v=[0]*6**8
r=s=0
while s<n:t,p=map(int,input().split());v[s+t]=max(v[s+t],r+p);s+=1;r=max(r,v[s])
print(r)