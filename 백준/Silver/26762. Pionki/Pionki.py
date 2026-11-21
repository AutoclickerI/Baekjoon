_,*l=open(0)
s=sorted
print(sum(s(map(str.count,l,z:='#'*10**6))[:-1]+s(map(tuple.count,zip(*l),z))[:-1]))