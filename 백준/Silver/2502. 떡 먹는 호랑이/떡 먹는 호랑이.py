d,k=map(int,input().split())
x=-1
for a in[y:=1]*d:x,y=y,x+y
while(b:=k-a*x)%y:a+=1
print(a,"\n",b//y)