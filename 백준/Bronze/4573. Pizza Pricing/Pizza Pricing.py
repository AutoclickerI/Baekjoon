i=0
while n:=int(input()):
 m=0;i+=1
 while n:
  n-=1;d,p=map(int,input().split());c=d*d/p
  if m<c:a=d;m=c
 print(f'Menu {i}:',a)