from itertools import*
c=0
print(0-max((sum(x)%10,c:=c+1)for i in[*open(0)][1:]for x in combinations(map(int,i.split()),3))[1]//-10)