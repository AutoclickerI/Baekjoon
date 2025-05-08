a=int(input())
if a<3:y=3
elif a<4:y=5
elif a<5:y=6
else:x=0;y=1;exec('x,y=y,x+y;'*a)
print(y-2)