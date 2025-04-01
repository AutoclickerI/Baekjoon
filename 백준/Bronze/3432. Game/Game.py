import re
r,j=range,''.join
for i in r(int(input())):
    l=[input()for _ in r(5)]
    a={*re.findall(r'(A|B)\1\1',' '.join(l+[*map(j,zip(*l))]+[j(l[-1-y+x][x] for x in r(5) if 0<=y-x<5) for y in r(2,7)]+[j(l[y-x][x] for x in r(5) if 0<=y-x<5) for y in r(2,7)]))}
    x,*y=a
    print('%s wins'%x if len(a)==1 else'draw')