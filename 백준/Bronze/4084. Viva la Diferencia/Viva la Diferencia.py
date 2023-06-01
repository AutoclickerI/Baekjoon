for i in[*open(0)][:-1]:
    *l,=map(int,i.split())
    n=0
    while len(set(l))-1:
        l=[abs(l[0]-l[1]),abs(l[1]-l[2]),abs(l[2]-l[3]),abs(l[3]-l[0])]
        n+=1
    print(n)