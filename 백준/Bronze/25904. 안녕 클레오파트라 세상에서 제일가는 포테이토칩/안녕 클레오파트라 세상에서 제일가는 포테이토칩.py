n,x,*l=map(int,open(i:=0).read().split())
while l[i%n]>=i+x:i+=1
print(i%n+1)