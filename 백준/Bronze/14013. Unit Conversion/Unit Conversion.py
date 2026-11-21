x,_,*l=open(0)
x,y=map(eval,x.split())
for i in l:print(eval(i[:-2])*[x/y,y/x][i[-2]<'B'])