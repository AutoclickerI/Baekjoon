from decimal import*
while s:=Decimal(input()):
 i=Decimal(2)
 while(s:=s-1/i)>0:i+=1
 print(i-1,'card(s)')