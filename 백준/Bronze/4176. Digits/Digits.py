for i in[*open(0)][:-1]:
    c=2
    if i=='1\n':
        print(1)
        continue
    i=str(len(i)-1)
    while'1'<i:
        i=str(len(i))
        c+=1
    print(c)