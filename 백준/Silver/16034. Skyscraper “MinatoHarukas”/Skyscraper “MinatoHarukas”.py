while b:=int(input())*2:
 for n in range(int(b**.5),0,-1):
  a,r=divmod(b-~-n*n,2*n)
  if r<1:print(a,n);break