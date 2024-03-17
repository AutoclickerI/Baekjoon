for i in[*open(0)][:-1]:
    v,n,m,a=*map(eval,i.split()),16
    for i in range(3):a=[50,500,3000][i]*((n-m)%10**(i+2)<1)or a
    print('%.2f'%(float(v)*a*(~-n%100//4==~-m%100//4)))