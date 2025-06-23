_,*l,(*o,_)=open(0)
x=y=0
for i in o:q='DUR'.find(i)*2;z=x+q//3,y+q%3-1;x,y=[z,(x,y)]['%d %d\n'%z in l]
print(x,y)