x,y,r,z,v,q,g,h,l=map(int,open(0).read().split())
j=k=.002;p=j*2
s=0
while j<99:
 while k<99:s+=p*p*((j-x)**2+(k-y)**2<r**2or(j-z)**2+(k-v)**2<q**2or(j-g)**2+(k-h)**2<l**2);k+=p
 k=p/2;j+=p
print(s)