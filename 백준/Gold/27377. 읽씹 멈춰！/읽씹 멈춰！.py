I=input
for a in[0]*int(I()):
 n,s,t=map(int,[I()]+I().split())
 while n:
  if n%2:a+=s;n-=1
  else:n//=2;a+=min(t,n*s)
 print(a) 