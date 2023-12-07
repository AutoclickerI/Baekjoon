t=0
for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    t+=p*60+q
m=1e9
for i in range(100):
    for j in range(100):
        if i*240+j*180>=t:
            m=min(10.9*i+9.15*j,m)
print(f'{m:.2f}')