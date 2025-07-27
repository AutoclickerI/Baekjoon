next(x:=open(0))
for _,i,j in zip(x,x,x):m,y,u,s,f,b,g,c,w=map(int,(i+j).split());print(min(2*m,2*y,4*u,16*s,16*f//9,b+g//30+c//25+w//10))