f=lambda y,x:10*x+y+100*((x==y)+2*([x,y]==[2,1]))
g=sorted
while(i:=input())>'1':a,b,*c=map(int,i.split());s,r=f(*g((a,b))),f(*g(c));print([f"Player {2-(s>r)} wins.","Tie."][s==r])