for *x,_ in[*open(0)][1:]:
    b=s=p=i=S=0
    for d in x:
        s+=int(d,36)
        if s//10!=p:
            p=s//10
            if p<4:b+=p
            else:S=p
    print(f"{b}{[['(weapon)','(09)'][S>4],''][S<1]}")