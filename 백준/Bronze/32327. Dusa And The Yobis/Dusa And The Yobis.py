n,*l=map(int,open(0))
f=1
for i in l:f&=i<n;n+=f*i
print(n)