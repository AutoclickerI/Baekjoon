a=[[sum(x),*map(x.count,[3,2])]for x in zip(*(map(int,i.split())for i in[*open(0)][1:]))]
b,c=sorted(a)[1:]
print((b<c)*-~a.index(c),c[0])