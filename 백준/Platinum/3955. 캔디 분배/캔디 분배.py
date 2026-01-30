for i in[*open(0)][1:]:
    K,C=map(int,i.split())
    try:
        if C==1:
            v=K+1
        elif K==1:
            v=C-1
        else:
            v=pow(C,-1,K)
        if 10**9<v:
            print('IMPOSSIBLE')
        else:
            print(v)
    except:
        print('IMPOSSIBLE')