for i in range(int(input())):
    print(f'Case #{i+1}:')
    N=int(input())
    *l,=map(int,input().split())
    a=[0]*N
    for k in range(N):
        v=[0]*N
        while v[k]<1:
            v[k]=1
            a[k]+=1
            k=l[k]-1
    print(*a)