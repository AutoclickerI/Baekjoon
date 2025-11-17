while n:=int(input()):
 k=eval('input(),'*n);c=0
 while len(k)==n:c+=1;k={i[1:]for i in k}-{''}
 print(c-(0<c))