def diff(a,b):
    ci=sum(i==j for i,j in zip(a,b))
    sq=sum(min(b.count(i),a.count(i))for i in{*a})
    return ci,sq-ci

for _ in[0]*int(input()):
    possible=['%04d'%i for i in range(10000)]
    _,*l=map(int,input().split())
    for v,ci,sq in zip(*[iter(l)]*3):
        v='%04d'%v
        possible=[i for i in possible if (ci,sq)==diff(v,i)]
    if len(possible)==1:
        print('The secret is:',*possible)
    else:
        if len(possible)>10:
            print('There is no guess that can uniquely identify the secret.')
        else:
            for i in range(10000):
                if len(possible)==len({diff('%04d'%i,j)for j in possible}):
                    print('There is a guess that can uniquely identify the secret:','%04d'%i)
                    break
            else:
                print('There is no guess that can uniquely identify the secret.')