idx=0
for _ in[0]*int(input()):
    idx+=1
    _,T=map(int,input().split())
    a=0
    t=0
    c=0
    for i in sorted(map(int,input().split())):
        if t+i<=T:
            t+=i
            a+=t
            c+=1
    print(f'Case {idx}:',c,t,a)