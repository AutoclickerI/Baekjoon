i=0
I=input
while(s:=int(I()))>0:i+=1;M=X=Y=0;exec("x,y,m=map(int,I().split());M+=m;X+=x*m;Y+=y*m;"*s);print(f'Case {i}: {X/M:.2f} {Y/M:.2f}');I()