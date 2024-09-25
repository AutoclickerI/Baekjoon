for s in[*open(0)][1:]:
    s=s[:-1]
    for i in'aeiou':s=s.replace(i,' ')
    for i in'qzwsxdcrfvtgbyhnjmklp':s=s.replace(i,'.')
    s=s.strip('.')
    *l,=map(len,s.split())
    a=1
    if s:
        for i in l:
            a=a*(i+1)%(10**9+7)
    else:
        a=-1
    print(a)