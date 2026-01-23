_,A,*l=[[*map(int,i.split())]for i in open(0)]
p=[0]
for i in sorted(A):p+=p[-1]+i,
for s,e in l:print(p[e]-p[s-1])