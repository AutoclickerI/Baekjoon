n=r=len(s:=input())
while(n%r<1)*n<r*r:r-=1
for i in range(r):print(end=s[i::r])