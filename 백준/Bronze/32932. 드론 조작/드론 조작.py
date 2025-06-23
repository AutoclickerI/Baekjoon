_,*l,o=open(0)
x=y=0
for i in o[:-1]:
 q='DUR'.find(i)*2;z=x+q//3,y+q%3-1
 if'%d %d\n'%z not in l:x,y=z
print(x,y)