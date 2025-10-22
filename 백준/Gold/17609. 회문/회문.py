def is_p(s,e,c):
    while s<e:
        if v[s]==v[e]:
            s+=1
            e-=1
        elif c<1:
            return min(is_p(s,e-1,1),is_p(s+1,e,1))
        else:
            return 2
    return c

for v in[*open(0)][1:]:
    print(is_p(0,len(v)-2,0))