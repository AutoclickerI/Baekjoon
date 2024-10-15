for i in[*open(0)][1:]:
    g,m=i.split(',')
    m=int(m)
    print(g,'-')
    for i,v in enumerate((525600,1440,60,1)):m>=v!=print(m//v,['year','day','hour','minute'][i]+'(s)');m%=v