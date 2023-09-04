for i in[*open(0)][:-1]:
    s=sum(sorted(map(int,i.split()))[1:5])
    if s%4:print(s/4)
    else:print(s//4)