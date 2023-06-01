for i in[0]*int(input()):
 n,k=map(int,input().split())
 r=1%n
 k=k%n
 for i in range(33):
  if r==0:print(i);break
  r=r*k%n
 if r!=0:print('unbounded')