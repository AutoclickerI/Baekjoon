for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    print(''.join(map(str,range(p,q+1))).count('0'))