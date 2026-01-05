[N,Ha],*l=[[*map(int,i.split())]for i in open(0)]

def sim():
    Hcur=m
    Hatk=Ha
    for t,a,h in l:
        if t==1:
            hit=-(-h//Hatk)-1
            if Hcur<=hit*a:
                return 0
            Hcur-=hit*a
        else:
            Hatk+=a
            Hcur=min(Hcur+h,m)
    return 1

s=0
e=10**18
while 1<e-s:
    m=s+e>>1
    if sim():
        e=m
    else:
        s=m
print(e)