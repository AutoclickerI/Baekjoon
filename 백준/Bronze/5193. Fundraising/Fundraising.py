for T in range(int(input())):
    c,d,t=map(int,input().split())
    buf=eval('[0]*c,'*d)
    for _ in range(t):
        di,ci,mi=map(int,input().split())
        buf[di-1][ci-1] += mi
    
    violators = []
    for i in range(d):
        Sum = 0
        for num in buf[i]:
            Sum += num
            if num > 2100 or Sum > 40000:
                violators+=i+1,
                break
    print(f'Data Set {T+1}:')
    if violators:
        print('Violators:')
        for Violator in violators:
            print(Violator)
    else:
        print('No violations')