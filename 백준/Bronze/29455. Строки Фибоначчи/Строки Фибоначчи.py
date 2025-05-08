x=0
y=1
exec('x,y=y,x+y;'*int(input()))
print(+(x<2)or y-min(2,x-2))