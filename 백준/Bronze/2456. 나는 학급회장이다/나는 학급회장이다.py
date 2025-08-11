a=[[sum(x),*map(x.count,[3,2])]for x in zip(*[map(int,i[::2])for i in open(0)][1:])]
_,b,c=sorted(a)
print((b<c)*-~a.index(c),c[0])