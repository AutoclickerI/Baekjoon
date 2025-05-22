for i in[*open(0)][1:]:
 i,j,k=map(int,i.split());a=0
 while k:a+=(k%j)**2;k//=j
 print(i,a)