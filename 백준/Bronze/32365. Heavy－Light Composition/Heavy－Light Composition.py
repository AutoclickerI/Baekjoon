for i in[*open(0)][1:]:
    d={}
    i=i[:-1]
    for j in i:d[j]=d.get(j,0)+1
    p=[2>d[j]for j in i[::2]];q=[2>d[j]for j in i[1::2]]
    print('FT'[all(p)and not any(q) or all(q)and not any(p)])