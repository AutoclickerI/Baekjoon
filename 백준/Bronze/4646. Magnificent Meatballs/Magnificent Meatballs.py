while(s:=input())[0]!='0':
    N,*l=map(int,s.split())
    a,b=0,sum(l)
    f=1
    for i in range(N-1):
        a+=l[i];b-=l[i]
        if a==b:
            print(f'Sam stops at position {i+1} and Ella stops at position {i+2}.')
            f=0
            break
    if f:print('No equal partitioning.')