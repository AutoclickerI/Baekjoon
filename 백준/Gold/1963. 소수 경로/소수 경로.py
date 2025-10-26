*p,=range(10000)

for i in range(2,10000):
    if p[i]:
        p[2*i::i]=[0]*len(p[2*i::i])

for i in[*open(0)][1:]:
    s,e=map(int,i.split())
    l=[(0,s)]
    v={s}
    for c,n in l:
        if n==e:break
        for i in range(4):
            x=[n//1000,n%1000//100,n%100//10,n%10]
            for j in range(10):
                x[i]=j
                nn=1000*x[0]+100*x[1]+10*x[2]+x[3]
                if x[0] and p[nn]and nn not in v:
                    v|={nn}
                    l+=(c+1,nn),
    else:
        print('Impossible')
        continue
    print(c)