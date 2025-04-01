for i in[*open(0)][2::2]:
    l=sorted(map(int,i.split()))
    print('YNeos'[1<=abs(sum(l)/len(l)-(l[0]+l[-1])/2)::2])