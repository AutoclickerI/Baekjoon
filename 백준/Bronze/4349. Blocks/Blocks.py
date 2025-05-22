for i in[*open(0)][1:]:
    i=int(i)
    m=2+4*i
    for w in range(1,i+1):
        if i%w<1:
            for h in range(1,i//w+1):
                if i//w%h<1:
                    m=min(m,2*w*h+i//w//h*2*(w+h))
    print(m)