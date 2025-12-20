N,M,*l=map(int,open(0).read().split())
w=c=0
for i in l:w=(w+i<=M)*w+i;c+=w==i
print(N and c)