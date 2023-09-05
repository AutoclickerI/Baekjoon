for i in[*open(0)][1:]:
    _,*l=map(int,i.split())
    s=sum(i%2*i for i in l);S=sum(l)-s
    print(['TIE','EVEN','ODD'][(s<S)-(s>S)])