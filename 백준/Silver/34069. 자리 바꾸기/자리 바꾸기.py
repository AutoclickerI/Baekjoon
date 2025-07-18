(N,M),*l=[[*map(int,i.split())]for i in open(0)]
if N*M%2:print('No')
else:
    print('Yes')
    if N%2:*l,=zip(*l)
    l[::2],l[1::2]=l[1::2],l[::2]
    if N%2:*l,=zip(*l)
    for i in l:print(*i)