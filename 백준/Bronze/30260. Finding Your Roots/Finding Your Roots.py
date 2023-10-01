for i in range(int(input())):
    a,_=map(int,input().split())
    *l,=map(int,input().split())
    ans=0
    while a:
        ans+=1
        a=l[a-1]
    print(f'Data Set {i+1}:')
    print(ans)
    print()