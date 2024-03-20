for i in[*open(0)][1:]:
    *l,=map(int,i.split())
    for i in range(19)[::-1]:l[i]+=l[i+1]//2;l[i+1]%=2
    print(*l)