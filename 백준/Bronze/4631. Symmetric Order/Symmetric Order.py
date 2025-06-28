T=0
while n:=int(input()):print('SET',T:=T+1);s=eval('input(),'*n);print(*s[::2]+s[1::2][::-1])