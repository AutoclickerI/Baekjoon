while n:=int(input()):
 a=k=0
 while n:k+=1;a+=n%10*(2**k-1);n=n//10
 print(a)