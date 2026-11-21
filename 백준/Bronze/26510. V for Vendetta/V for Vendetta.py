for i in map(int,input().split()):
 n=i
 while n-1:print(' '*(i-n)+'*'+' '*(2*n-3)+'*');n-=1
 print(' '*(i-1)+'*')