for i in[*open(t:=0)][1:]:
    t+=1
    p,q=map(int,i.split())
    p-=1
    print(f'Data Set {t}:')
    if p<q:
        print(end='no ')
    else:
        while(p:=p//5)>q:
            print(end='mega ')
    print('drought\n')