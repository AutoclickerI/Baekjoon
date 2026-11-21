for T in range(int(input())):
    input();m=-1;l=*map(int,input().split()),-1;a=0
    for i,j in zip(l,l[1:]):
        if i>m:
            m=i
            a+=i>j
    print(f'Case #{T+1}:',a)