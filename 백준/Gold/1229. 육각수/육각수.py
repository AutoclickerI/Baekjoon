h=[]
s=0
n=int(input())
d=[0,1,2,3,4,5,1,2,3,4,5,6,2]
while(l:=(s:=s+1)*(2*s-1))<=n:h+=[l]
if n<13:print(d[n])
else:
 for i in range(13,n+1):
  m=10**9
  for p in h:
   if p>i:break
   m=min(m,d[i-p])
  d+=[m+1]
 print(d[n])