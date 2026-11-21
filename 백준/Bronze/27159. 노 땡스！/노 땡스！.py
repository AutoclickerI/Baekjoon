_,*l=map(int,open(0).read().split())
a=c=0
for i in l:a+=i*(i-c>1);c=i
print(a)