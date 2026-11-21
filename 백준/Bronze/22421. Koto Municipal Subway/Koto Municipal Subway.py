while(s:=input())!='0 0':
    D,E=map(int,s.split())
    m=101
    for i in range(D):
        m=min(abs((i*i+(D-i)**2)**.5-E),m)
    print(m)