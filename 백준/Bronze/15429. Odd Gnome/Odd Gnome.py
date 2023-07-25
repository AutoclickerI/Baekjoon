for i in[*open(0)][1:]:
    *l,=map(int,i.split())
    for j in range(l[0]):
        if l[j+2]-l[j+1]!=1:
            print(j+2)
            break
    