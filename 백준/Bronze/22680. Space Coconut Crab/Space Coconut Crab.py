while e:=int(input()):
    m=1e6
    p=int((e+0.9)**(1/3))
    for z in range(p+1):
        y=int((e-z**3)**.5)
        m=min(m,e-y*y-z**3+y+z)
    print(m)