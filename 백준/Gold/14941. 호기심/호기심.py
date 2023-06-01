l=[*range(2<<17)]
for i in range(2,10**5):
 if l[i]:
  n=i
  while n<10**5:l[(n:=n+i)]=0
L=[l[i]for i in range(1,10**5)if l[i]]
S1=[2]
S2=[3]
for i,j in enumerate(L[3:]):
 if i%2:S2+=[S2[-1]+j]
 else:S1+=[S1[-1]+j]
S1+=[0]
S2+=[0]
from bisect import*
for i in[*open(0)][1:]:
 p,q=map(int,i.split())
 p,q=bisect_left(L, p),bisect_right(L, q)
 if p>q:print(0)
 else:
  q=max(1,q)-2;p=max(1,p)-2
  if p%2:o,e=S2[(q-1)//2]-S2[p//2],S1[q//2]-S1[p//2]
  else:o,e=S1[q//2]-S1[p//2],S2[(q-1)//2]-S2[(p-2)//2]
  print(e*3-o)