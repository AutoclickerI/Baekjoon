n,x,*l=map(int,open(i:=0).read().split())
while x<=l[i%n]:x+=1;i+=1
print(i%n+1)