for _ in[0]*int(input()):
    v=0
    f=1
    for i in input():
        v+=sum(map(int,str(int(i)*(1+f))))
        f^=1
    print('FT'[v%10<1])