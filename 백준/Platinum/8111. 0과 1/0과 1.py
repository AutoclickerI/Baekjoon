for i in[*open(0)][1:]:
    n=int(i)
    v=[0]*n
    r=1%n
    v[r]=1
    l=[(r,1)]
    for r,s in l:
        if r<1:
            print(f'{s:b}')
            break
        if 1<<99<=s:
            continue
        for i in 0,1:
            nr=(r*10+i)%n
            if v[nr]<1:
                v[nr]=1
                l+=(nr,s<<1|i),
    else:print('BRAK')