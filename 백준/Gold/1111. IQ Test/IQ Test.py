p=print
n,i,*l=map(int,open(0).read().split())
n>2or exit(p(['A',i][n==2and i==l[0]]))
a=l[0]-i
if a:a=(l[1]-l[0])//a
b=l[0]-i*a
[x*a+b==y or exit(p('B'))for x,y in zip(l,l[1:])]
p(a*l[-1]+b)