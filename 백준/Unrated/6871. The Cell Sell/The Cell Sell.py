a,b,c=map(int,open(0))
d=5*max(0,a-100)+3*b+4*c
e=9*max(0,a-250)+7*b+5*c
p=print;f='Plan';g='costs'
p(f,'A',g,d/20)
p(f,'B',g,e/20)
p([f+f' {"AB"[d>e]} is cheapest.',f+' A and B are the same price.'][d==e])