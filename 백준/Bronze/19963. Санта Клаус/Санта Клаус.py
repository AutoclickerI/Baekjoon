n,_,_,*l=map(int,open(0).read().split())
s={*range(1,n+1)}
for i in l:s.discard(i)
print(len(s),*s)