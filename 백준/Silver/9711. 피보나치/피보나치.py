for i in[*open(c:=0)][1:]:
 P,Q=map(int,i.split());a=1;b=0;c+=1
 while P:P-=1;a,b=a+b,a%Q
 print(f'Case #{c}:',b)