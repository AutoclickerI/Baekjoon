n,*l=map(int,open(0).read().split())
l.sort()
s=sum(l)
i=v=m=0
while l:v+=l.pop();i+=1;m=max(m,v/s-i/n)
print(m*100)