p=print
n,i,*l=map(int,open(0).read().split())
n<3>exit(p([i,'A'][n<2or i!=l[0]]))
Q,*Z=l
b=Q-i
a=b and(l[1]-Q)//b
b-=i*~-a
for x,y in zip(l,Z):x*a+b!=y>exit(p('B'))
p(a*l[-1]+b)