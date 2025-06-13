for i in[*open(0)][1:]:
    s,c=i.split()
    l=[i*j for i,j in zip(map(c.count,'BCMW'),(2,1,4,3))]
    if l.count(max(l))-1:
        print(s+':','There is no dominant species')
    else:
        print(s+':','The',['Bobcat','Coyote','Mountain Lion','Wolf'][l.index(max(l))],'is the dominant species')
    