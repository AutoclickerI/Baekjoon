f=int.bit_length
while n:=int(input()):
 r=''
 while 1<n:r=f'{n:b}'+r;n=f(n)-1
 print('0'+r)