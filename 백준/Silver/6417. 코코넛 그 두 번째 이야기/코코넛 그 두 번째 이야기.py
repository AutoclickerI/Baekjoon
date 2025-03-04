while~(n:=int(input())):
 s='no solution'
 for k in range(1,9):
  if(n+(-k)**k+k)%k**-~k==1:s=f'{k} people and 1 monkey'
 print(n,'coconuts,',s)