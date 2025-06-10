for *x,_ in[*open(0)][1:]:
    b=s=p=i=0;S=''
    for d in x:
        s+=int(d,36)
        if s//10!=p:
            p=s//10
            if p<4:b+=p
            else:S=['(weapon)','(09)'][p>4]
    print(f'{b}'+S)