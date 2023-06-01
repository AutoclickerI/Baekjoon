for i in[*open(0)][1:]:
    p=int(i[:2])
    q=int(i[2:])
    if(p*p+q*q)%7==1:
        print('YES')
    else:print('NO')