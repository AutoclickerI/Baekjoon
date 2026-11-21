m=n=int(input())
l=input().split()+['1']
s='R'*n
i=-1
while(i:=i+1)<n:
 if l[i]=='0':
  t=l.index('1',i);H=i+n-t
  if H+i<m:m=H+i;s='L'*i+'R'*H
  if(k:=2*H-i)<m:m=k;s='R'*(n-t)+'L'*H
  i=t
print(m,s)