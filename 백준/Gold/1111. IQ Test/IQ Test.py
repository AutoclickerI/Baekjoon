p=print
n,i,*l=map(int,open(0).read().split())
n>2or exit(p(['A',i][n==2and i==l[0]]))
b=l[0]-i
a=b and(l[1]-l[0])//b
b-=i*~-a
for x,y in zip(l,l[1:]):x*a+b!=y>exit(p('B'))
p(a*l[-1]+b)