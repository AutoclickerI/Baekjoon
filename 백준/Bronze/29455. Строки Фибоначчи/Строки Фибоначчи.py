a=int(input())
x=0;y=1;exec('x,y=y,x+y;'*a)
print(+(a<3)or y-2+max(0,5-a))