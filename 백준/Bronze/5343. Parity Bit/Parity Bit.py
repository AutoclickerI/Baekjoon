for i in[*open(0)][1:]:
    a=0
    while'\n'!=i:
        p,i=i[:8],i[8:]
        a+=eval('^'.join(p))
    print(a)