for i in zip(*[*open(0)][1:]):
    d={'\n':-1}
    for j in i:d[j]=d.get(j,0)+1
    for j in sorted(d):
        if d[j]==max(d.values()):
            print(end=j)
            break