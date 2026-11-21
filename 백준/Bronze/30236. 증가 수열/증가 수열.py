for i in[*open(0)][2::2]:
    s=0
    for j in i.split():
        s+=1
        s+=int(j)==s
    print(s)