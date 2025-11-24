from itertools import*
c,*r=0,
for i in[*open(0)][1:]:
 c+=1
 for x in combinations(map(int,i.split()),3):r+=(sum(x)%10,c),
print(max(r)[1])