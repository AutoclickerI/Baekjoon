for s in[*open(0)][1:]:
    c=0
    p=s[0]
    for i in s:
        if i!=p:print(c,end=p);c=1
        else:c+=1
        p=i
    print()