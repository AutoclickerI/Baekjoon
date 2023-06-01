_,*l=map(int,open(0))
l.sort()
m=-1
while l:t=sum(L:=l[-3:]);m=t*(m<t>2*max(L))or m;l.pop()
print(m)