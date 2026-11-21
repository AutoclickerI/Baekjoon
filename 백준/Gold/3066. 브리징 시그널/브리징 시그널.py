from bisect import*
I=input
for i in[0]*int(I()):
 n=int(I());l=[int(I())for i in[0]*n];d=[m:=0];c=[-2e+9]
 for i in range(n):
  if c[-1]<l[i]:c+=[l[i]];d+=[m:=len(c)-1]
  else:d+=[bisect_left(c,l[i])];c[d[-1]]=l[i]
 print(m)