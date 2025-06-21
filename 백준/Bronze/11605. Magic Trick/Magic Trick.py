_,*A=open(s:=0).read().split()
O=[*zip(A[::2],map(int,A[1::2]))]
for i in range(100):
 i+=1
 for o,n in O:
  match o[0]:
   case'A':i+=n
   case'S':i-=n
   case'M':i*=n
   case'D':i/=n
  if i%1 or i<0:s+=1;break
print(s)