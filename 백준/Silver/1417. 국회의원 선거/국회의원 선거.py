_,A,*l=*map(int,open(d:=0)),0
while(x:=max(l))>=A+d:l[l.index(x)]-=1;d+=1
print(d)