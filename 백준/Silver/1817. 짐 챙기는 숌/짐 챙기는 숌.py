N,M,*l=map(int,open(0).read().split())
w=c=0
for i in l:f=M<w+i;w+=i-f*w;c+=f
print(N and-~c)