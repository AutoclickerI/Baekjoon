x,y,r,z,v,q,g,h,l=map(int,open(0).read().split())
p=j=k=2e-3
s=0
while j<99:
 while k<99:
  if(j-x)**2+(k-y)**2<r**2or(j-z)**2+(k-v)**2<q**2or(j-g)**2+(k-h)**2<l**2:s+=4*p*p
  k+=2*p
 k=p;j+=2*p
print(s)