_,*l=[map(int,i.split())for i in open(0)]
s={}
for x,y,X,Y in l:s|={(i,j):1for i in range(x,X+1)for j in range(y,Y+1)}
print(len(s))