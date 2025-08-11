n=r=len(s:=input())
while r>n/r or n%r>0:r-=1
for i in range(r):print(end=s[i::r])