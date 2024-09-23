while n:=int(input()):
 a,s,i=0,3,2
 while n>=s:a+=(n-s)%i<1;i+=1;s+=i
 print(a)