while'0'<(n:=input()):
  n=int(n)
  l,r,*s=1,50
  while l<=r:
    m=(l+r)//2;s.append(m)
    if m==n:break
    elif m<n:l=m+1
    else:r=m-1
  print(*s)