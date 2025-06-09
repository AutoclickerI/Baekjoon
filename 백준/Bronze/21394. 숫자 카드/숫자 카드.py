for i in[*open(0)][1:]:
    l=sorted(''.join(j*int(k)for j,k in zip('123459789',i.split())))[::-1]
    v=[[],[]]
    f=0
    for i in l:
        v[f]+=i,
        f^=1
    s,e=v
    print(*s,*e[::-1])