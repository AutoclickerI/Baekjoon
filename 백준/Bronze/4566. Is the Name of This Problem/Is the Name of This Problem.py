for i in[*open(0)][:-1]:
    f=i.count('" ')==1 and i.count('"')==2
    if f:
        p,q=i.split('" ')
    if f*p[0]=='"'and p[1:]==q[:-1]:print(f'Quine({p[1:]})')
    else:print('not a quine')