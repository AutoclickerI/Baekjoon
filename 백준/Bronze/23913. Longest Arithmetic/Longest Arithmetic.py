for T in range(int(input())):
    input()
    m=1
    p=1e18
    v=1e99
    for i in map(int,input().split()):
        if v-i==p:
            a+=1
        else:
            a=2
            p=v-i
        m=max(a,m)
        v=i
    print(f'Case #{T+1}:',m)