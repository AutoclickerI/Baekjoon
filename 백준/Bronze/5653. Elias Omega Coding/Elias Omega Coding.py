while n:=int(input()):
 r=''
 while 1<n:r=f'{n:b}'+r;n=n.bit_length()-1
 print('0'+r)