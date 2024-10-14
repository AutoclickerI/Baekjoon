l=[50,20,10,5,1]
for i in[*open(0)][1:]:
    m=-eval(i.replace(*' -'))
    b=[]
    for c in l:q,m=divmod(m,c);b+=int(q),
    t=[]
    for i,j in zip(b,l):t+=f'{i}-${j}',
    print(*t,sep=', ')