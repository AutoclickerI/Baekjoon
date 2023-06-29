for i in[*open(0)][1:]:
    n,*l=map(int,i.split())
    print(f'{100*sum(i*n>sum(l)for i in l)/n:.3f}%')