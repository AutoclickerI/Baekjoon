r=range(n:=int(input()))
for x in r:print(''.join('* '[not{0,n-1}&{x,y,y+x,x-y}]for y in r))