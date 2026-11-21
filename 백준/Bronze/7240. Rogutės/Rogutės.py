_,S,*l,a=map(int,open(s:=0).read().split())
for i in l:s+=i;s-=s>S
print(s+a)