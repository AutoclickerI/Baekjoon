while m:=int(input()):
 a=b=c=1
 while(a,b)!=(0,1):a,b=b,(a+b)%m;c+=1
 print(m,c)