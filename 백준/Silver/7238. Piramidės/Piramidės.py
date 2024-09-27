N=int(input())
while N:
 c=h=0
 while c<N:h+=1;N+=~c;c+=1
 print(h)