for i in[*open(0)][1:]:
    i=m=int(i)
    while i!=1:
        m=max(i:=[i//2,i*3+1][i%2],m)
    print(m)