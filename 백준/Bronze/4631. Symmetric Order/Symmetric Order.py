T=0
while n:=int(input()):s=eval('input(),'*n);print('SET',T:=T+1,*s[::2]+s[~(n%2)::-2])