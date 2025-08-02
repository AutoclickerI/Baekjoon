while'0'<(m:=input()):
 n=int(m);l,r,*s=1,50
 while m!=n:
  print(m:=l+r>>1)
  if m<n:l=m+1
  else:r=m-1