l=[*map(int,open(0).read().split())][:-3]
while l:a,b,c,*l=l;a,b,c=sorted([a,b,c]);print(['Invalid','Equilateral','Isosceles','Scalene'][(a+b>c)*len({a,b,c})])