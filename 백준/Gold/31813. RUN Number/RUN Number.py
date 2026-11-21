for i in[*open(0)][1:]:
    K=i.split()[1]
    l=[]
    while 1:
        if len(K)<2:
            if'0'<K:l+=K
            break
        if int(K)<int(K[0]*len(K)):
            if K[0]=='1':
                v=int('9'*(len(K)-1))
            else:
                v=int(str(int(K[0])-1)*len(K))
        else:
            v=int(K[0]*len(K))
        l+=v,
        K=str(int(K)-v)
    print(len(l))
    print(*l)